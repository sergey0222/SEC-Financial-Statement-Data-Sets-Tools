# lists all tags used in a given adsh

import datetime
import csv
import h5py as h5
import datasets_lib as ds

# the line below is needed to prevent the following error: field larger than field limit (131072)
csv.field_size_limit(10000000)

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# set path to folder Datasets/
path = 'D:/DataSets/'

# we are looking for all the tags for this adsh (given as int)
adsh_int = 23200 

# and also print out all of these tags appearances
tag_int = 248

# initialize tags list
tag_list = []

# load tag names
index_tag=ds.list_from_file(path+'/reindexed/index_tag.txt')
  
# find all tags
with open(path + 'filter_1/filter_1_num.txt') as f:
#with open(path + 'reindexed/reindexed_num.txt') as f:
        f_object = csv.reader(f, delimiter='\t')
        for row in f_object:

            # check if current record is for a given adsh
            if int(row[0]) == adsh_int:
                # if yes, add original string version of tag to the list               
                tag_list.append(index_tag[int(row[1])])
                if int(row[1]) == tag_int:
                    print(row)

print('Number of different tags for this adsh is:', len(tag_list))
ds.list_to_file(tag_list, path + 'other/all_tags_for_adsh.txt')
print(tag_list[0:20])
# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)    
            
           

            
            
            
            
            
