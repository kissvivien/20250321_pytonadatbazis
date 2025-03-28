import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

DATABASE = "mydatabase"
mycursor.execute(F"CREATE DATABASE IF NOT EXISTS {DATABASE}")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute(F"USE {DATABASE}")  