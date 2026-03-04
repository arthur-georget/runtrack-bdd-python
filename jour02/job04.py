import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="youruser",
  password="yourpassword",
  database="laplateforme"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT nom, capacite FROM salle;")

print(mycursor.fetchall())

mycursor.close()
mydb.close()