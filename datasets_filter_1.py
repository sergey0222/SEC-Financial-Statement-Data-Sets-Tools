'''
This filter module looks through all lines in reindexed_sub.txt & reindexed_num.txt and extracts only those which the following is true::
- fiscal year ends on Dec 31
- report is 10-K
- tag belongs to us-gaap taxonomy
- data relates to point in time (qtrs=0) or to 4 quartes (qtrs=4)
- unit of measure is USD or Shares
- full year reports exist for all years starting from 'first' and ending with 'last'
The following files are saved in /filter_1 folder:
- filter_1_sub.txt
- filter_1_num.txt
- report_adsh.h5 (see description below)   

'''
import datetime
import csv
import numpy as np
import h5py as h5
import datasets_lib as ds

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# the line below is needed to prevent the following error: field larger than field limit (131072)
csv.field_size_limit(10000000) 

# set path to folder Datasets/
path = 'D:/DataSets/'

# the folowing part constructs report_bool adn report_adsh matrixes with similar dimensions:
# - column number corresponds to reindexed cik
# - row number correponds to the year of the report (first eligible year correspondsm to row 0)
# report_bool contains True if for the given cik and given year full year report exists
# report_adsh contains adsh values (int) of those reports

# first and last years to take into consideration
start = 2008
end = 2019

# load cik and adsh lists
list_cik = ds.list_from_file(path + 'reindexed/index_cik.txt')
list_adsh = ds.list_from_file(path + 'reindexed/index_adsh.txt')

# initialize matrixes
report_bool = np.zeros((len(list_cik),end-start+1), dtype=bool)
report_adsh = np.zeros((len(list_cik),end-start+1), dtype=int)

# this list will remember the year for a given adsh
adsh_year = [''] * len(list_adsh)

# fills in both matrixes
with open(path + '/reindexed/reindexed_sub.txt') as f:
    f_object = csv.reader(f, delimiter='\t')
    for row in f_object:
        
        adsh = row[0]
        cik = row[1]
        fye = row[24]
        form = row[25]
        period = row[26]
        fy = row[27]
        fp = row[28]
        
        if fye == '1231' and form == '10-K' and period[4:8] == '1231' and fy != '' and int(fy) >= start and int(fy) <= end and fp == 'FY': 
                                        
            # row index corresonds to cik
            r = int(cik)

            # column index corresponds to year offset 
            c = int(fy) - start            

            # mark corresponding combination of cik and year as eligible
            report_bool[r,c] = True
            report_adsh[r,c] = int(adsh)
            
            adsh_year[int(adsh)] = fy 


# count how many companies have FY reports in the indicated year range

# define the final year in a range
last = 2018

print('Number of companies for which full year reports exist for all years in a range:')
for i in range (start, last + 1):
    
    # define first year
    first = i
    
    # cut out unneeded years
    report_bool_cut = report_bool[:,first - start : last - start + 1]
    
    # define ciks for which all FY reports in a given range exist
    mask = np.all(report_bool_cut, axis=1)
    number = np.sum(mask)
    print(i, '-', last, ':', number)

# define years taking part in X creation 
first = 2011
last = 2018   

# cut off all unneeded years
report_bool_cut = report_bool[:,first - start : last - start + 1]
report_adsh_cut = report_adsh[:,first - start : last - start + 1]

# define ciks for which all FY reports in a given range exist
mask1D = np.all(report_bool_cut, axis=1, keepdims = True)

# creates mask for extracting eligible adsh
mask2D = np.logical_and(report_bool_cut, mask1D)

# extract all eligible adsh into an array
elig_adsh_ind = np.extract(mask2D, report_adsh_cut)

# creates a list of all adsh with the relevant ones being True
elig_adsh = np.zeros((len(list_adsh),1), dtype = bool)
elig_adsh[elig_adsh_ind] = True

# creates filter_1_num.txt with relevant lines only

# initialize counters
lines_num_original = 0
lines_num_filtered = 0

print('Sorting out tags...')
with open(path + 'Filter_1/filter_1_num.txt', 'w', newline='') as filter_1_num:
    filter_1_num_object = csv.writer(filter_1_num, delimiter='\t')

    with open(path + 'Reindexed/reindexed_num.txt') as reindexed_num:
        reindexed_num_object = csv.reader(reindexed_num, delimiter='\t')
        
        for row in reindexed_num_object:

            lines_num_original += 1
            
            adsh = row[0]
            version = row[2]
            coreg = row[3]
            ddate = row[4]
            qtrs = row[5]
            uom = row[6]
            value = row[7]
            
            if elig_adsh[int(adsh)] and version[0:7] == 'us-gaap' and coreg == '' and ddate[0:4] == adsh_year[int(adsh)] and ddate[4:8] == '1231' and value != '':
                if qtrs == '0' or qtrs == '4':
                    if uom == 'USD' or uom == 'shares':
                        filter_1_num_object.writerow(row)
                        lines_num_filtered += 1

# creates filter_1_sub.txt with relevant lines only
                        
# initialize counters
lines_sub_original = 0
lines_sub_filtered = 0                        
                        
with open(path + 'filter_1/filter_1_sub.txt', 'w', newline='') as filter_1_sub:
    filter_1_sub_object = csv.writer(filter_1_sub, delimiter='\t')

    with open(path + 'reindexed/reindexed_sub.txt') as reindexed_sub:
        reindexed_sub_object = csv.reader(reindexed_sub, delimiter='\t')
        
        for row in reindexed_sub_object:
            lines_sub_original += 1
            adsh = row[0]
            if elig_adsh[int(adsh)]:
                filter_1_sub_object.writerow(row)
                lines_sub_filtered += 1
                
# writes report_adsh into report_adsh.h5 
with h5.File(path + '/filter_1/elig_adsh_ind.h5', 'w') as hf:
    hf.create_dataset('elig_adsh_ind',  data = elig_adsh_ind)              
            
# print statistics
print('Number of filtered/original lines sub files:', lines_sub_filtered, lines_sub_original)
print('Number of filtered/original lines num files:', lines_num_filtered, lines_num_original)

# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)





