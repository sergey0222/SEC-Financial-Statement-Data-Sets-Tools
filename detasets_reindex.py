# This module reindexes important fields to be represented by continuous space

import datetime
import csv
import datasets_lib as ds


# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# the line below is needed to prevent the following error: field larger than field limit (131072)
csv.field_size_limit(10000000) 

# set path to folder Datasets/
# the structure of this folder is as follows:
# /Datasets/Originals/ - set of original datasets folders 2009q1, 2009q2, ....
# /Datasets/Explore/ - output files of this module

path = 'D:/DataSets/'
folders = ('2009q1','2009q2','2009q3','2009q4','2010q1','2010q2','2010q3','2010q4','2011q1','2011q2','2011q3','2011q4','2012q1','2012q2','2012q3','2012q4','2013q1','2013q2','2013q3','2013q4','2014q1','2014q2','2014q3','2014q4','2015q1','2015q2','2015q3','2015q4','2016q1','2016q2','2016q3','2016q4','2017q1','2017q2','2017q3','2017q4','2018q1','2018q2','2018q3','2018q4','2019q1')
#folders = ('2018q1','2018q2') # for testing

# initialize lists for storing original values
list_adsh = []
list_cik = []
list_tag = []

# initialize dictionaries for indexing via tree
dic_adsh = {}
dic_cik = {}
dic_tag = {}


# initialize variables
next_ind_adsh = 0
next_ind_cik = 0
next_ind_tag = 0

# the following part reindexes all sub.txt files and stores them in a single file /Reindexed/reindexed_sub.txt
with open(path + 'Reindexed/reindexed_sub.txt', 'w', newline='') as reindexed_sub:
    reindexed_sub_object = csv.writer(reindexed_sub, delimiter='\t')

    for i in range(len(folders)):
        print('working on', folders[i]+'/sub.txt...')
        with open(path + 'Originals/' + folders[i] + '/sub.txt') as f:
            f_object = csv.reader(f, delimiter='\t')
            
            # skip header line
            next(f_object)
            
            for row in f_object:
              
                # work on adsh field
                adsh = row[0]
                ind, next_ind_adsh = ds.index_by_tree(adsh, dic_adsh, next_ind_adsh)
                # if index is out of the current list, append the list with count 1. Otherwise increase the count by 1
                if ind == len(list_adsh):
                    list_adsh.append(adsh)
                row[0] = str(ind)
                            
                # cik
                cik = row[1]
                ind, next_ind_cik = ds.index_by_tree(cik, dic_cik, next_ind_cik)
                if ind == len(list_cik):
                    list_cik.append(cik)
                row[1] = str(ind) 
                    
                reindexed_sub_object.writerow(row)

# the following part reindexes all num.txt files and stores them in a single file /Reindexed/reindexed_num.txt
with open(path + 'Reindexed/reindexed_num.txt', 'w', newline='') as reindexed_num:
    reindexed_num_object = csv.writer(reindexed_num, delimiter='\t')

    for i in range(len(folders)):
        print('working on', folders[i]+'/num.txt...')
        with open(path + 'Originals/' + folders[i] + '/num.txt') as f:
            f_object = csv.reader(f, delimiter='\t')
            
            # skip header line
            next(f_object)
            
            for row in f_object:
              
                # work on adsh field
                adsh = row[0]
                ind, next_ind_adsh = ds.index_by_tree(adsh, dic_adsh, next_ind_adsh)
                # if index is out of the current list, append the list with count 1. Otherwise increase the count by 1
                if ind == len(list_adsh):
                    list_adsh.append(adsh)
                row[0] = str(ind)
                            
                # tag
                tag = row[1]
                ind, next_ind_tag = ds.index_by_tree(tag, dic_tag, next_ind_tag)
                if ind == len(list_tag):
                    list_tag.append(tag)
                row[1] = str(ind) 
                    
                reindexed_num_object.writerow(row)               

# save new indexes
ds.list_to_file(list_adsh, path + 'Reindexed/index_adsh.txt')
ds.list_to_file(list_cik, path + 'Reindexed/index_cik.txt')
ds.list_to_file(list_tag, path + 'Reindexed/index_tag.txt')

# print statistics
print('Total number of reports (adsh):', len(list_adsh))
print('Total number of unique companies (cik):', len(list_cik))
print('Total number of unique tags in all reports (tag):', len(list_tag))

# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)





