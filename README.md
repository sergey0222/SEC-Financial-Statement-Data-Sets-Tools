# SEC-Financial-Statement-Data-Sets-Tools
Tools for working with U.S. Securities and Exchange Commission Financial Statement Data Sets.

U.S. Securities and Exchange Commission (SEC) provides numeric information from all the financial statements filed to the commission since January 2009. The link to the datasets is here: https://www.sec.gov/dera/data/financial-statement-data-sets.html

This repository provides tools which I developed for the data alalysis. The tools are used for:
- getting statistics of different kind (number of companies, filings, tags, etc.)
- reindexing several fields for speeding up the calculations
- presening the information in a specific format to feed to other sytems (e.g. machine learning frameworks)

The first tool called datsets_explorer runs through all the files and analyses the most important fields. The details can be found in the file itself. Below you may find the current statistics for 2009q1 ... 2019q1 filings:
- Total number of reports (adsh): 235 179
- Total number of unique companies (cik): 12 521
- Number of different industries (sic): 435
- Number of countries of incorporation (countryinc): 56
- Number of different filing reports (form): 49
- Total number of unique tags in all reports (tag): 1 371 759
- Number of different Units of Measure (uom): 6 393
- Total number of lines in all sub.txt files: 235 179
- Total number of lines in all num.txt files: 87 753 960

A predefined file structure is used in all tools to be consistent:

Datasets - root folder (pointed by variable 'path')
- Originals - original files from the link above unzipped to folders 2009q1, 2009q2 ...
- Explore - the output of Explore mudule
- Reindexed - reindexed dataset files
- Filter_1 - files after applying filter datasets_filter_1 (see details in the module itself)

