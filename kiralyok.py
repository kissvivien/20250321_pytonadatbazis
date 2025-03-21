from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='kiralyok')
#táblák megjelenítése
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print (table)    
print ("-------")

#uralkodok megjelenítése    
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print (uralkodo)            
print ("-------")

cursor.execute("SELECT * FROM uralkodo WHERE nev = 'I. Mátyás'")
for uralkodo in cursor:
    print (uralkodo)
print ("-------")    

cursor.execute("SELECT * FROM uralkodo WHERE nev = 'I. Mátyás'")
for uralkodo in cursor:
    print (f"Mátyás király élt: {uralkodo [0]} - {uralkodo[1]}")
print ("-------")    

cnx.close()