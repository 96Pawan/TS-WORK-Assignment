# TSWORKS  ASSIGNMENT
Data Load -

Download the finance data from five companies of your choice:
Sample URL for IBM - https://finance.yahoo.com/quote/IBM/history?p=IBM

Download should be automated via code.
The list of companies should be configurable using a config file.
This is to ensure that there is flexibility to add more companies with minimal code changes
The data should be loaded to a single table in a DB (sqllite, postgres, my sql).
You can add more columns if you need.
Data can be inserted or updated if the same rows already exist.
You can write a SQL function to accomplish this.

 

Data APIs-

Write below APIs end points using flask or fast framework:
Get all companies’ stock data for a particular day (Input to API would be date)
Get all stock data for a particular company for a particular day (Input to API would be company ID/name and date)
Get all stock data for a particular company (Input to API would be company ID/name)
POST/Patch API to update stock data for a company by date.
