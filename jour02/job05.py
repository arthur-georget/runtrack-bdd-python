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

mycursor.execute("SELECT SUM(superficie) FROM etage;")

print(f"La superficie de La Plateforme est de {mycursor.fetchall()[0][0]} m2")

mycursor.close()
mydb.close()