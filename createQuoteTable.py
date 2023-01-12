# import files needed to connect to database
import mysql.connector
import dbconfig as cfg


db = mysql.connector.connect(
  host = cfg.mysql['host'],
  user = cfg.mysql['user'],
  password = cfg.mysql['password']
  database = "quote"
)

# Connect to db, enter sql, execute and close connection
cursor = db.cursor()
sql="CREATE TABLE quote (id INT AUTO_INCREMENT PRIMARY KEY, quote VARCHAR(250), author VARCHAR(250))"

cursor.execute(sql)

db.close()
cursor.close()