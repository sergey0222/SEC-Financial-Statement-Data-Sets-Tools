# this is a test file
import csv
import datasets_lib as ds

list_out = ['1','2','3','4','5','6']
ds.list_to_file(list_out,"test.txt")

list_in = ds.list_from_file('test.txt')
print(list_in)


