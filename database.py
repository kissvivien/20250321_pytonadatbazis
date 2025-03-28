import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

#ADATBÁZIS LÉTREHOZÁSA
DATABASE = "mydatabase"
mycursor.execute(F"CREATE DATABASE IF NOT EXISTS {DATABASE}")

# ADATBÁZISOK MUTATÁSA
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

#HASZNÁLD EZT AZ ADATBÁZIST
mycursor.execute(F"USE {DATABASE}") 

#CUSTOMERS TÁBLA LÉTREHOZÁSA
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
P("-------")

#TÁBLÁK MUTATÁSA
mycursor.execute("SHOW TABLES ")

for x in mycursor:
  print(x)