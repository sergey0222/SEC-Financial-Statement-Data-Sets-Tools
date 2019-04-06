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

path = ('D:/DataSets/')
folders = ('2009q1','2009q2','2009q3','2009q4','2010q1','2010q2','2010q3','2010q4','2011q1','2011q2','2011q3','2011q4','2012q1','2012q2','2012q3','2012q4','2013q1','2013q2','2013q3','2013q4','2014q1','2014q2','2014q3','2014q4','2015q1','2015q2','2015q3','2015q4','2016q1','2016q2','2016q3','2016q4','2017q1','2017q2','2017q3','2017q4','2018q1','2018q2','2018q3','2018q4','2019q1')
#folders = ('2018q1','2018q2') # for testing

# initialize lists for gathering statistics
list_adsh = []
list_cik = []
list_sic = []
list_countryinc = []
list_changed_year = []
list_fye = []
list_form = []
list_fp = []
list_prevrpt = []
list_nciks = []
list_tag = []
list_version = []
list_coreg = []
list_qtrs = []
list_uom = []

# initialize lists for indexing
dic_adsh = {}
dic_cik = {}
dic_sic = {}
dic_countryinc = {}
dic_changed_year = {}
dic_fye = {}
dic_form = {}
dic_fp = {}
dic_prevrpt = {}
dic_nciks = {}
dic_tag = {}
dic_version = {}
dic_coreg = {}
dic_qtrs = {}
dic_uom = {}

# initialize variables
next_ind_adsh = 0
next_ind_cik = 0
next_ind_sic = 0
next_ind_countryinc = 0
next_ind_changed_year = 0
next_ind_fye = 0
next_ind_form = 0
next_ind_fp = 0
next_ind_prevrpt = 0
next_ind_nciks = 0
next_ind_tag = 0
next_ind_version = 0
next_ind_coreg = 0
next_ind_qtrs = 0
next_ind_uom = 0

# initialize number of lines counters
lines_in_sub = 0
lines_in_num = 0

# the following part exporers sub.txt files for all periods
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
                list_adsh.append([1,adsh])
            else:
                list_adsh[ind][0] += 1
                        
            # cik
            cik = row[1]
            ind, next_ind_cik = ds.index_by_tree(cik, dic_cik, next_ind_cik)
            if ind == len(list_cik):
                list_cik.append([1,cik])
            else:
                list_cik[ind][0] += 1    
                
            # sic
            sic = row[3]
            ind, next_ind_sic = ds.index_by_tree(sic, dic_sic, next_ind_sic)
            if ind == len(list_sic):
                list_sic.append([1,sic])
            else:
                list_sic[ind][0] += 1
 
            # countryinc
            countryinc = row[17]
            ind, next_ind_countryinc = ds.index_by_tree(countryinc, dic_countryinc, next_ind_countryinc)
            if ind == len(list_countryinc):
                list_countryinc.append([1,countryinc])
            else:
                list_countryinc[ind][0] += 1
             
            # changed (year only!)    
            changed_year = row[21][0:4]
            ind, next_ind_changed_year = ds.index_by_tree(changed_year, dic_changed_year, next_ind_changed_year)
            if ind == len(list_changed_year):
                list_changed_year.append([1,changed_year])
            else:
                list_changed_year[ind][0] += 1
                
            # fye
            fye = row[24]
            ind, next_ind_fye = ds.index_by_tree(fye, dic_fye, next_ind_fye)
            if ind == len(list_fye):
                list_fye.append([1,fye])
            else:
                list_fye[ind][0] += 1
                
            # form
            form = row[25]
            ind, next_ind_form = ds.index_by_tree(form, dic_form, next_ind_form)
            if ind == len(list_form):
                list_form.append([1,form])
            else:
                list_form[ind][0] += 1                  
                
            # fp
            fp = row[28]
            ind, next_ind_fp = ds.index_by_tree(fp, dic_fp, next_ind_fp)
            if ind == len(list_fp):
                list_fp.append([1,fp])
            else:
                list_fp[ind][0] += 1 
                
            # prevrpt
            prevrpt = row[31]
            ind, next_ind_prevrpt = ds.index_by_tree(prevrpt, dic_prevrpt, next_ind_prevrpt)
            if ind == len(list_prevrpt):
                list_prevrpt.append([1,prevrpt])
            else:
                list_prevrpt[ind][0] += 1                
                                
            # nciks
            nciks = row[34]
            ind, next_ind_nciks = ds.index_by_tree(nciks, dic_nciks, next_ind_nciks)
            if ind == len(list_nciks):
                list_nciks.append([1,nciks])
            else:
                list_nciks[ind][0] += 1
                
            lines_in_sub += 1    

# the following part exporers num.txt files for all periods
for i in range(len(folders)):
    print('working on', folders[i]+'/num.txt...')
    with open(path + 'Originals/' + folders[i] + '/num.txt') as f:
        f_object = csv.reader(f, delimiter='\t')
        
        # skip header line
        next(f_object)

        for row in f_object:
          
            # tag
            tag = row[1]
            ind, next_ind_tag = ds.index_by_tree(tag, dic_tag, next_ind_tag)
            if ind == len(list_tag):
                list_tag.append([1,tag])
            else:
                list_tag[ind][0] += 1  
                
            # version
            version = row[2]
            ind, next_ind_version = ds.index_by_tree(version, dic_version, next_ind_version)
            if ind == len(list_version):
                list_version.append([1,version])
            else:
                list_version[ind][0] += 1                  
                
            # coreg
            coreg = row[3]
            ind, next_ind_coreg = ds.index_by_tree(coreg, dic_coreg, next_ind_coreg)
            if ind == len(list_coreg):
                list_coreg.append([1,coreg])
            else:
                list_coreg[ind][0] += 1  

            # qtrs
            qtrs = row[5]
            ind, next_ind_qtrs = ds.index_by_tree(qtrs, dic_qtrs, next_ind_qtrs)
            if ind == len(list_qtrs):
                list_qtrs.append([1,qtrs])
            else:
                list_qtrs[ind][0] += 1 
                
            # uom
            uom = row[6]
            ind, next_ind_uom = ds.index_by_tree(uom, dic_uom, next_ind_uom)
            if ind == len(list_uom):
                list_uom.append([1,uom])
            else:
                list_uom[ind][0] += 1

            lines_in_num += 1                 

# save all the lists to files
ds.list_to_file (list_adsh, path + 'Explore/list_adsh.txt')
ds.list_to_file (list_cik, path + 'Explore/list_cik.txt')
ds.list_to_file (list_sic, path + 'Explore/list_sic.txt')
ds.list_to_file (list_countryinc, path + 'Explore/list_countryinc.txt')
ds.list_to_file (list_changed_year, path + 'Explore/list_changed_year.txt')
ds.list_to_file (list_fye, path + 'Explore/list_fye.txt')
ds.list_to_file (list_form, path + 'Explore/list_form.txt')
ds.list_to_file (list_fp, path + 'Explore/list_fp.txt')
ds.list_to_file (list_prevrpt, path + 'Explore/list_prevrpt.txt')
ds.list_to_file (list_nciks, path + 'Explore/list_nciks.txt')
ds.list_to_file (list_tag, path + 'Explore/list_tag.txt')
ds.list_to_file (list_version, path + 'Explore/list_version.txt')
ds.list_to_file (list_coreg, path + 'Explore/list_coreg.txt')
ds.list_to_file (list_qtrs, path + 'Explore/list_qtrs.txt')
ds.list_to_file (list_uom, path + 'Explore/list_uom.txt')

# print statistics
print('Total number of reports (adsh):',len(list_adsh))
print('Total number of unique companies (cik):', len(list_cik))
print('Number of different industries (sic):', len(list_sic))
print('Number of countries of incorporation (countryinc):', len(list_countryinc))
print('Number of different filing reports (form):', len(list_form))
print('Total number of unique tags in all reports (tag):', len(list_tag))
print('Number of different Units of Measure (uom):', len(list_uom))
print('Total number of lines in all sub.txt files:', lines_in_sub)
print('Total number of lines in all num.txt files:', lines_in_num)

# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)





