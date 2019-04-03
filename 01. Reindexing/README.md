THe scope, organization, file formats and table definitions for the datasets can be found on SEC's website as .PDF file at the following link: https://www.sec.gov/files/aqfs.pdf

In order for the tool to work download and unzip all files from SEC's website (https://www.sec.gov/dera/data/financial-statement-data-sets.html) to a local folder on your computer named Datasets. You will have a list of folders 2009q1, 2009q2, ... up to the most current folder. Assigne variable 'path' in the beginning of the program the path to these folders on your computer (e.g. in my case path = 'D:/Datasets/')

Run the program.

It outputs the following files in /Datasets/reindexed/
- sub_reindexed.txt (sub.txt from all folders combined into one file with adsh, cik, and uom changed to new numeric indexes)
- num_reindexed.txt (num.txt from all folders combined with adsh and tag changed to new numeric indexes)
- adsh.txt (list of all unique adsh values, line number in the file corresponds to the new numeric index)
- cik.txt (list of all unique cik values, line number in the file corresponds to the new numeric index)
- tag.txt (list of all unique tag values, line number in the file corresponds to the new numeric index)
- uom.txt (list of all unique uom values, line number in the file corresponds to the new numeric index)

The program also shows the statistics for the current dataset.
For 2009q1...2018q4 it is as follows:
- number of unique ciks = 
- number of unique adshs = 
- number of unique tags = 
- number of unique uoms = 
