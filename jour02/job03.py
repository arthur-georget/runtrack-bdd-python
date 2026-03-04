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

mycursor.execute("INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500), ('R+1', 1, 500);")
mycursor.execute("INSERT INTO salle (nom, id_etage, capacite) VALUES ('Lounge', 1, 100), ('Studio Son', 1, 5), ('Broadcasting', 2, 50), ('Bocal Peda', 2, 4), ('Coworking', 2, 80), ('Studio Video', 2, 5);")

mydb.commit()

mycursor.close()
mydb.close()