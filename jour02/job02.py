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

mycursor.execute("CREATE TABLE etage (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom VARCHAR(255), numero INT, superficie INT);"
                 "CREATE TABLE salle (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom VARCHAR(255), id_etage INT, capacite INT);")

mycursor.close()
mydb.close()