from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='oscar')

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)