import pandas as pd
from bs4 import BeautifulSoup
import requests, os, json, re, csv
import mysql.connector, pymysql
from sqlalchemy import create_engine
import dbconfig as cfg


def __init__(self):
    self.host=       cfg.mysql['host']
    self.user=       cfg.mysql['user']
    self.password=   cfg.mysql['password']
    self.database=   cfg.mysql['database']
# get the page and extract HTML using requests library:
#f = requests.get('http://quotes.toscrape.com/')


# pass the site's HTML to BeautifulSoup to be parsed:
#soup = BeautifulSoup(f.text)

# All of the site's data is now stored in the soup object

# Find all the divs with the 'quote' class and all the spans within the 
# divs with the 'text' class.
"""for i in soup.findAll("div",{"class":"quote"}):
    print((i.find("span",{"class":"text"})).text)"""

# Now scrape Author names by looking for the 'quote' divs with the class of 'author' within them.
"""for i in soup.findAll("div",{"class":"quote"}):
    print((i.find("small",{"class":"author"})).text)"""

# Create empty arrays for quotes and authors:
quotes = []
authors = []

# The website has 10 pages. Create a loop from 1 to 10 to go 
# through every page and iterate over the HTML, extracting the quotes and authors 
# and append to an array.
for pages in range(1,10):
    g = requests.get('http://quotes.toscrape.com/page/'+str(pages))
    soup = BeautifulSoup(g.text)    
for i in soup.findAll("div",{"class":"quote"}):
    quotes.append((i.find("span",{"class":"text"})).text)  
   
for j in soup.findAll("div",{"class":"quote"}):
    authors.append((j.find("small",{"class":"author"})).text)   
    #for k in soup.findAll("div",{"class":"tags"}):
    #tags.append((k.find("meta"))['content'])
#print(quotes)
#print(soup.get_text())

# Import into a pandas dataframe:
quotesdf = pd.DataFrame(
    {'Quotes':quotes,
    'Authors':authors
    })

json_quotes = quotesdf.to_json

# Get the current directory
currentDir = os.path.dirname(os.path.realpath(__file__))

# read csv and put into DataFrame
column_names = ['id','Quote', 'Author']

df = pd.read_csv(f'{currentDir}/quotes.csv', quotechar='"', doublequote=True, quoting = csv.QUOTE_NONNUMERIC, header = None, names = column_names)

# Remove Nan and other values
df = df.drop(df.index[:1])

# Change id from float to integer
df['id'] = df['id'].astype(float).astype(int)

# Escape quotes
df['Quote'] = df['Quote'].str.replace('"','')

# Check
print(df.tail(2))

# First set of values
df1 = df.iloc[:10]
x1 = df1.tail(9)
#print(x1)

# second set of values
df2 = df.iloc[11:100]
x2 = df2.tail(89)

# Why 2 sets of values? Error being thrown. Above is a hack.
val_to_insert = x1.values.tolist()
val_to_insert2 = x2.values.tolist()
#print(val_to_insert)
#print(val_to_insert2)


#print(val_to_insert)
#df = pd.read_csv(f'{currentDir}/quotes.csv', header = 0)
#print(df)



# Trying from 
# https://softhints.com/insert-multiple-rows-at-once-with-python-and-mysql/

con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['user'], passwd=cfg.mysql['password'], db=cfg.mysql['database'], charset='utf8')
cursor = con.cursor()

cursor.executemany("insert into quote (id, Quote, Author) values (%s, %s, %s)",
                   val_to_insert)

cursor.executemany("insert into quote (id, Quote, Author) values (%s, %s, %s)",
                   val_to_insert2)

con.commit()
con.close()