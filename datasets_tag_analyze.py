# Calculates how much tags are missing in the eligible reports

import datetime
import csv
import h5py as h5
import datasets_lib as ds

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# set path to folder Datasets/
path = 'D:/DataSets/'

# initialize tag_count list for counting tags
list_tag=ds.list_from_file(path+'/reindexed/index_tag.txt')
tag_count = []
for i in range(len(list_tag)):
    tag_count.append([0,i])
  
# collect tag's statistics
with open(path + 'filter_1/filter_1_num.txt') as f:
        f_object = csv.reader(f, delimiter='\t')
        for row in f_object:
           tag = row[1]
           tag_count[int(tag)][0] += 1
           
tag_count.sort(reverse = True)

# load elig_adsh_ind list and calculate total number of eligible reports
with h5.File(path + '/filter_1/elig_adsh_ind.h5', 'r') as hf:
    elig_adsh_ind = hf['elig_adsh_ind'][:]
elig_reports = len(elig_adsh_ind)

for i in range(20):
    tag = tag_count[i][1]
    tag_name = list_tag[tag]
    percent = round(tag_count[i][0] / elig_reports * 100, 0)
    print(percent, '% of reports contain tag',tag_name)
    
# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)    
            
           

            
            
            
            
            
