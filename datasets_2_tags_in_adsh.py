# returns a list of adshs which contain 2 give tags

import datetime
import numpy as np
import csv
import h5py as h5
import datasets_lib as ds

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# set path to folder Datasets/
path = 'D:/DataSets/'

# given tags as original string
tag_to_look_1 = 'NetIncomeLoss'
tag_to_look_2 = 'ProfitLoss'

# load index_tag
index_tag=ds.list_from_file(path+'/reindexed/index_tag.txt')

# get reindexed value of the tag
tag_to_look_1_int = index_tag.index(tag_to_look_1)
tag_to_look_2_int = index_tag.index(tag_to_look_2)

# load a list of all adshs
index_adsh=ds.list_from_file(path+'/reindexed/index_adsh.txt')

# create an array for marking adshs
adsh_mark = np.zeros((len(index_adsh),2), dtype = bool)
  
# collect adsh statistics
with open(path + 'filter_1/filter_1_num.txt') as f:
        f_object = csv.reader(f, delimiter='\t')
        for row in f_object:
            
            adsh_int = int(row[0])
            tag_int = int(row[1])

            # is it the tag we are looking for?
            if tag_int == tag_to_look_1_int:
                # if yes, mark corresponding adsh as used
                adsh_mark[adsh_int,0] = True
                
            if tag_int == tag_to_look_2_int:
                adsh_mark[adsh_int,1] = True                

# create vector with True elements for adsh for which both tags exist
adsh_mark_all = np.all(adsh_mark, axis=1, keepdims=True)

# load elig_adsh_list
with h5.File(path + 'filter_1/elig_adsh_list.h5', 'r') as hf:
    elig_adsh_list = hf['elig_adsh_list'][:]                

# create a mask of eligible adsh
elig_adsh_mask =  np.zeros((len(index_adsh),1), dtype = bool) 
elig_adsh_mask[elig_adsh_list] = True
  
# create a vector with True for adsh which we are looking for
result = np.logical_and(elig_adsh_mask, adsh_mark_all)

# extract adsh indexes
valid_adsh_list = np.nonzero(result)[0]

print('Number of adsh for which both tags exist:',len(valid_adsh_list))
print('First 20 entries of the list:')
print(valid_adsh_list[0:20])
        
# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)    
            
     

            
            
            
            
            
