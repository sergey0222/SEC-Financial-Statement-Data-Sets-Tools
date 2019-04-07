# This module looks through all lines in reindexed_num.txt and extracts only values related to Full Year reports
# with fiscal year coinsiding with the calendar year

import datetime
import csv
import datasets_lib as ds

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# the line below is needed to prevent the following error: field larger than field limit (131072)
csv.field_size_limit(10000000) 

# set path to folder Datasets/

path = 'D:/DataSets/'

# load index_adsh.txt
list_adsh = ds.list_from_file(path + 'Reindexed/index_adsh.txt')

# create empty list which contain fp field for all adsh
fp_list = [''] * len(list_adsh)

with open(path + 'Reindexed/reindexed_sub.txt') as reindexed_sub:
    reindexed_sub_object = csv.reader(reindexed_sub, delimiter='\t')
    
    for row in reindexed_sub_object:
        
        adsh = row[0]
        fp = row[28]
        
        fp_list[int(adsh)] = fp

# initialize counters
lines_original = 0
lines_filtered = 0

with open(path + 'Filter_1/filter_1_num.txt', 'w', newline='') as filter_1_num:
    filter_1_num_object = csv.writer(filter_1_num, delimiter='\t')

    with open(path + 'Reindexed/reindexed_num.txt') as reindexed_num:
        reindexed_num_object = csv.reader(reindexed_num, delimiter='\t')
        
        for row in reindexed_num_object:

            lines_original += 1
            
            adsh = row[0]
            version = row[2]
            coreg = row[3]
            ddate = row[4]
            qtrs = row[5]
            uom = row[6]
            value = row[7]
            
            if version[0:7] == 'us-gaap' and coreg == '' and ddate[4:8] == '1231' and value != '' and fp_list[int(adsh)] == 'FY':
                if qtrs == '0' or qtrs == '4':
                    if uom == 'USD' or uom == 'shares':
                        filter_1_num_object.writerow(row)
                        lines_filtered += 1

# print statistics
print('Number of lines in the original file', lines_original)
print('Number of lines in the filtered file', lines_filtered)

# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)





