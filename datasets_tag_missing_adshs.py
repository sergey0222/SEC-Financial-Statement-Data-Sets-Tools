# returns a list of adshs which do NOT contain a given tag for a prefiltered set

import datetime
import numpy as np
import csv
import h5py as h5
import datasets_lib as ds

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# set path to folder Datasets/
path = 'D:/DataSets/'

# given tag as original string
tag_to_look = 'Assets' 

# load index_tag
index_tag=ds.list_from_file(path+'/reindexed/index_tag.txt')

# get reindexed value of the tag
tag_to_look_int = index_tag.index(tag_to_look)

# load a list of all adshs
index_adsh=ds.list_from_file(path+'/reindexed/index_adsh.txt')

# create an array for marking adshs
# column 0 = True if this adsh is in fliter_1_num.txt file
# column 1 = True if rag_original is present in this adsh
adsh_mark = np.zeros((len(index_adsh),2), dtype = bool)
  
# collect adsh statistics
with open(path + 'filter_1/filter_1_num.txt') as f:
        f_object = csv.reader(f, delimiter='\t')
        for row in f_object:
            
            adsh_int = int(row[0])
            tag_int = int(row[1])
            
            # mark this adsh as present
            adsh_mark[adsh_int,0] = True

            # is it the tag we are looking for?
            if tag_int == tag_to_look_int:
                # if yes, mark corresponding adsh as used
                adsh_mark[adsh_int,1] = True


# create a vector with True for adsh which we are looking for
missing_adsh_bool = np.logical_and(adsh_mark[:,0], np.invert(adsh_mark[:,1]))               

# extract adsh indexes
missing_adsh_list = np.nonzero(missing_adsh_bool)[0]
print(missing_adsh_list[0:20])
        
# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)    
            
     

            
            
            
            
            
