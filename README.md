[![My Skills](https://skillicons.dev/icons?i=python,mysql,flask&theme=light)](https://skillicons.dev)
</i>



# Data-Representation-Project
The project for the Data Representation module at ATU.<br>

This particular project is about inspirational quotes, i.e.

## "Watchoo' talkin' about, Willis?"
#### [Arnold, Diff'rent Strokes](https://www.bing.com/ck/a?!&&p=f1dd64d283bcf503JmltdHM9MTY3MzY1NDQwMCZpZ3VpZD0wYzg5YzZjYS1jNDhlLTZlYmUtMjQ5Ni1kNzhhYzVjMzZmMzQmaW5zaWQ9NTE5NA&ptn=3&hsh=3&fclid=0c89c6ca-c48e-6ebe-2496-d78ac5c36f34&psq=whatchoo+talkin+bout+willis&u=a1aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1iSmQxUmt0allUVQ&ntb=1)


The user is able to create, update and delete quotes via the front-end (html page).


## Installation:

Clone repo onto your own machine.
Make sure that [flask is installed](https://flask.palletsprojects.com/en/1.1.x/installation/).

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


### final_scraper.py
This is a scraper, written in Beautiful Soup, that scrapes quotes from a website and puts it into the database, in the table specified. 
Running this allows the database to be pre-populated with quotes from historical figures.

### quoteDAO.py

This is the Database Access Object and is used to access the database. 


### quoteViewer.html

This is the html for the front-end page (the webpage) and makes AJAX calls to the database via quoteDAO

### quoteserver.py
This is the code for the server to run.
The curl commands have been left in, but commented out.


## Python Anywhere Installation:
[Python Anywhere](https://www.pythonanywhere.com/) is a service that allows users to run their (small) Python projects for free.<br>
The recommended way is to clone a github repository, and then use the in-built bash console to edit any files as necessary, i.e *db.config*.<br>
This was the order in which it was done:
1. Sign up for a python anywhere account (a free account)
2. Clone the github repository (this one)
3. Note that pythonanywhere automatically adds the prefix *user_name* + "$" before the database name - the database can be created via the graphical tool to avoid any issues.
4. edit *dbconfig.py* using [Vim](http://vimsheet.com/)
5. Create the table by typing *python createQuoteTable.py* at the bash prompt
6. Navigate to *Databases* and open a MySQL console (choose the one with the database name you created)
7. type "SHOW DATABASES"; and hit enter to verify the database is there
8. type "USE database_name" where database_name is the name of the database that you created
9. type "SHOW tables"; to verify that a table named 'quote' was created
10. Run: *python final_scraper.py* in the bash console
11. Go back to the mysql console and type: "SELECT * FROM quote"; to verify the scraper populated the database.
12. Follow instructions on python anywhere to host the site, but these are the important bits:
    - reference the file that calls Flask from the wsgi file.
    - erase the localhost references (127.0.0.1:5000) from the html file - otherwise, no quotes will be displayed.

[Here is the project hosted on pythonanywhere](http://irishfab.pythonanywhere.com/)

### Login details
user: andy1
password: pass2


### References

1. [Escaping double and single quotes in MySQL using Python](https://stackoverflow.com/questions/36512985/escaping-single-and-double-quotes-for-mysql-in-python)<br>
2. [Quotation marks appearing as question marks in MySQL](https://stackoverflow.com/questions/41043922/characters-appear-as-question-marks-in-mysql)<br>
3. [Bulma CSS Framework](https://bulma.io/)<br>
4. [MySQL connector errors](https://stackoverflow.com/questions/63689559/mysql-connector-errors-programmingerror-not-enough-parameters-for-the-sql-state)<br>
5. [Pandas DataFrame to SQL](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html)<br>
6. [Flask installation instructions](https://flask.palletsprojects.com/en/1.1.x/installation/)<br>
7. [Python Anywhere](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles)<br>
 []()<br>
 []()<br>
 []()<br>
