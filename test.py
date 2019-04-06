# this is a test file
import csv
import datasets_lib as ds

list_test = []
dic_test = {}
next_ind_test = 0

for j in range(5):
    test = ''
    ind, next_ind_test = ds.index_by_tree(test, dic_test, next_ind_test)
    if ind == len(list_test):
        list_test.append([1,test])
    else:
        list_test[ind][0] += 1

