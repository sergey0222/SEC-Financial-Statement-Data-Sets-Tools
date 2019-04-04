# SEC-Financial-Statement-Data-Sets-Tools
Tools for working with U.S. Securities and Exchange Commission Financial Statement Data Sets.

U.S. Securities and Exchange Commission (SEC) provides numeric information from all the financial statements filed to the commission since January 2009. The link to the datasets is here: https://www.sec.gov/dera/data/financial-statement-data-sets.html

This repository provides tools which I developed for the data alalysis. The tools are used for:
- getting statistics of different kind (number of companies, filings, tags for particular years, etc.)
- analyzing which tags (values) are present in a given set of reports
- preparing data as input for other systems (e.g. Machine Leraning Frameworks)

The first and most important is Reindexing tool. Why is reindexing needed for the datasets? The datasets containe 12K+ unique companies, 200K+ reports and 80M+ values (tags). Unfortunately the indexes used in the database (e.g. adsh, cik, tag name) are not easy to work with. E.g. adsh is a 20-character long and if you want to create a table in which eache value will be addressed individually you will not be able to fit the table into your computer memory. At the same time the number of unique adsh values is relatively small (200K+) which fits fine to almost every modern computer memory without any problems. 
More details to be found in folder 01. Reindexing.
      

To adanyze during Explore phase.
sub.txt:
- adsh
- cik
- sic
- contryinc
- changed (at least analyze year when the name was changed)
- fye (Fiscal Year End Date)
- form
- fp
- prevrpt
- nciks

num.txt:
- tag
- version
- coreg (at least empty/non-empty)
- qtrs
- uom
