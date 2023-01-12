# Data-Representation-Project
The project for the Data Representation module at ATU


## Installation:

Clone repo onto your own machine.
Make sure that flask is installed.

## Explanation of the files:

### dbconfig_template.py

This file needs to be renamed to *dbconfig.py*<br>
and needs to have the environment variables specific to you/your machine entered, for example:<br>
- hostname
- MySQL username
- MySQL password

### create_Database_FF.py

This file creates the MySQL database. It has to be run first in order to create the database for the project


### createQuoteTable.py

This has to be run after the database is created in order to create the database table for the project.


### quoteDAO.py

This is the Database Access Object and is used to access the database. 


### quoteViewer.html

This is the html for the front-end page (the webpage) and makes AJAX calls to the database via quoteDAO

### quoteserver.py
This is the code for the server to run.
The curl commands have been left in, but commented out.


###


###