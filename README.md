# SEC-Financial-Statement-Data-Sets-Tools
Tools for working with U.S. Securities and Exchange Commission Financial Statement Data Sets.

U.S. Securities and Exchange Commission (SEC) provides numeric information from all the financial statements filed to the commission since January 2009. The link to the datasets is here: https://www.sec.gov/dera/data/financial-statement-data-sets.html

This repository provides tools which I developed for the data alalysis. The tools are used for:
- getting statistics of different kind (number of companies, filings, tags, etc.)
- reindexing several fields for speeding up the calculations
- presening the information in a specific format to feed to other systems (e.g. here: https://github.com/sergey0222/Neural-Networks-and-Value-Investing)

The first tool called datasets_explore runs through all the files and analyses the most important fields. The details can be found in the file itself. Below you may find the current statistics for 2009q1 ... 2019q1 filings:
- total number of reports (adsh): 235179
- total number of unique companies (cik): 12521
- number of different industries (sic): 435
- number of countries of incorporation (countryinc): 56
- number of different filing reports (form): 49
- total number of unique tags in all reports (tag): 1371759
- total number of unique co-registrants (coreg): 35762
- number of different Units of Measure (uom): 6393
- total number of lines in all sub.txt files: 235179
- total number of lines in all num.txt files: 87753960

Currently the list of tools is as follows:
- datasets_explore - gets statistics for most of the data fields
- datasets_reindex - reindexes several fields to greatly speed up future processing
- datasets_filter_1 - filters out unneeded records accordning to the set of rules (see details in the module itself)
- datasets_lib - provides functions often used in the tools
- datasets_tag_analyze - gets statistics on how often different tags are used in pre-filtered reports
- datasets_tag_missing_adsh - returns a list of adshs which do NOT contain a given tag for a prefiltered set
- datasets_all_tags_for_adsh - returns a list of all tags in a given adsh
- datasets_show_adsh_details - prints details for a given adsh including links to SEC site
- datasets_2_tags_in_adsh - creates a list of adsh for which 2 given tags exist

A predefined file structure is used in all tools to be consistent:

Datasets - root folder pointed to by variable 'path'
- Datasets\Originals - original files from the link above unzipped to folders 2009q1, 2009q2 ...
- Datasets\Explore - the output of Explore mudule
- Datasets\Reindexed - reindexed dataset files
- Datasets\Filter_1 - files after applying filter datasets_filter_1 (see details in the module itself)
- Datasets\other - output of some smaller modules
