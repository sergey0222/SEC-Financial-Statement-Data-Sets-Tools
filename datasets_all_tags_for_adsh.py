# lists all tags used in a given adsh

import datetime
import csv
import h5py as h5
import datasets_lib as ds

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# set path to folder Datasets/
path = 'D:/DataSets/'

# we are looking for all the tags for this adsh (given as int)
adsh_int = 23476 

# initialize tags list
tag_list = []

# load tag names
index_tag=ds.list_from_file(path+'/reindexed/index_tag.txt')
  
# find all tags
with open(path + 'filter_1/filter_1_num.txt') as f:
        f_object = csv.reader(f, delimiter='\t')
        for row in f_object:
            # check if current record is for a given adsh
            if int(row[0]) == adsh_int:
                # if yes, add original string version of tag to the list               
                tag_list.append(index_tag(int(row[1])))

print(tag_list[0:20])
# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)    
            
           

            
            
            
            
            
