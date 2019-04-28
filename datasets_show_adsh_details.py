# lists all tags used in a given adsh

import datetime
import csv
import h5py as h5
import datasets_lib as ds

# store starting time for calculating total processing time
time_start = datetime.datetime.now()

# set path to folder Datasets/
path = 'D:/DataSets/'

# we are looking for this adsh
adsh_int = 23189 

index_adsh = ds.list_from_file(path + 'reindexed/index_adsh.txt') 
index_cik = ds.list_from_file(path + 'reindexed/index_cik.txt')

# find all tags
with open(path + 'reindexed/reindexed_sub.txt') as f:
        f_object = csv.reader(f, delimiter='\t')
                      
        # skip lines lines until adsh is found
        row = next(f_object)
        while int(row[0]) != adsh_int:
            row = next(f_object)
            continue
              
        print('Reindexed ADSH is:', adsh_int)
        
        adsh_org = index_adsh[adsh_int]
        print('Original ADSH is:', adsh_org)
        
        print('Reindexed CIK is:', row[1])
        
        cik_org = index_cik[int(row[1])]
        print('Original CIK is:', cik_org )
        
        print('Name of registrant:', row[2])
        print('Standard Industrial Classification, SIC:', row[3])
        print('Date of change from the former name, CHANGED:', row[21])
        print('Fiscal Year End Date, FYE:', row[24])
        print('The submission type of the registrant’s filing, FORM:', row[25])
        print('Balance Sheet Date, PERIOD:', row[26])
        print('Fiscal Year Focus, FY:', row[27])
        print('Fiscal Period Focus, FP:', row[28])
        print('The name of the submitted XBRL Instance Document, INSTANCE:', row[33])
        
        print('Link company page in EDGAR: https://www.sec.gov/cgi-bin/browse-edgar?CIK=' + cik_org + '&owner=exclude&action=getcompany&Find=Search')
        print('Link to this report page in EDGAR: https://www.sec.gov/Archives/edgar/data/' + cik_org + '/' + adsh_org.replace('-', '') + '/' + adsh_org + '-index.htm')
# processing time
print('time elapsed - ', datetime.datetime.now() - time_start)    
            
           

            
            
            
            
            
