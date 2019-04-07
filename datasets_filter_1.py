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

# initialize counters
line_original = 0
line_filtered = 0

with open(path + 'Filter_1/filter_1_num.txt', 'w', newline='') as filter_1_num:
    filter_1_num_object = csv.writer(filter_1_num, delimiter='\t')

    with open(path + 'Reindexed/reindexed_num.txt') as reindexed_num:
        reindexed_num_object = csv.reader(reindexed_num, delimiter='\t')
        
        for row in reindexed_num_object:

            line_original += 1
            
            version = row[2]
            coreg = row[3]
            ddate = row[4]
            qtrs = row[5]
            uom = row[6]
            value = row[7]
            
            if version[0:7] == 'us-gaap' and coreg != '' and ddate[4:8] == '1231' and value != '':
                if qtrs == '0' or qtrs == '4':
                    if uom == 'USD' or uom == 'shares':
                        filter_1_num_object.writerow(row)
                        line_filtered += 1

# print statistics
print('Number of lines in the original file', line_original)
print('Number of lines in the filtered file', line_filtered)

# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)





