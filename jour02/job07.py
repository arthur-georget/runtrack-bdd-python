import mysql.connector

class Employe:

    def __init__(self):
        self.__id = None
        self.__nom = None
        self.__prenom = None
        self.__salaire = None
        self.__id_service = None

    def get_id(self):
        return self.__id
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_salaire(self):
        return self.__salaire
    
    def get_id_service(self):
        return self.__id_service

    def create(self, nom: str, prenom: str, salaire: float, id_service: int):
        self.__nom = nom
        self.__prenom = prenom
        self.__salaire = salaire
        self.__id_service = id_service
        mycursor.execute(f"INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('{self.__nom}', '{self.__prenom}', {self.__salaire}, {self.__id_service})")
        self.__id = mycursor.lastrowid
        mydb.commit()

    def read(self, id: int):
        mycursor.execute(f"SELECT * from employe WHERE id = {id}")
        result = mycursor.fetchall()
        self.__id = id
        self.__nom = result[0][1]
        self.__prenom = result[0][2]
        self.__salaire = result[0][3]
        self.__id_service = result[0][4]

    def update_nom(self, nom: str):
        mycursor.execute(f"UPDATE employe SET {nom} WHERE id = {self.__id};")
        self.__nom = nom

    def update_prenom(self, prenom: str):
        mycursor.execute(f"UPDATE employe SET {prenom} WHERE id = {self.__id};")
        self.__prenom = prenom

    def update_salaire(self, salaire: float):
        mycursor.execute(f"UPDATE employe SET {salaire} WHERE id = {self.__id};")
        self.__salaire = salaire

    def update_id_service(self, id_service: int):
        mycursor.execute(f"UPDATE employe SET {id_service} WHERE id = {self.__id};")
        self.__id_service = id_service    

    def delete(self, id: int = None):
        if not id:
            id = self.__id
        mycursor.execute(f"DELETE FROM employe WHERE id = {id}")
        mydb.commit()


mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="youruser",
  password="yourpassword"
)

print(mydb)
mycursor = mydb.cursor()

def database_init():
    mycursor.execute("CREATE DATABASE lamegastartup;")
    mycursor.execute("USE lamegastartup;")
    mycursor.execute("CREATE TABLE service (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom VARCHAR(63));")
    mycursor.execute("CREATE TABLE employe (id INT NOT NULL AUTO_INCREMENT, nom VARCHAR(63), prenom VARCHAR(63), salaire DECIMAL, id_service INT NOT NULL, PRIMARY KEY(id), FOREIGN KEY (id_service) REFERENCES service(id));")
    mycursor.execute("INSERT INTO service (nom) VALUES ('IT'),('Admin'),('Prod');")
    mycursor.execute("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('DURAND','Bernie',3432,1),('TRAORE','Ali',4432,2),('TANG','Emmanuel','2023',3);")
    mydb.commit()

database_init()

mycursor.execute("USE lamegastartup;")

mycursor.execute("SELECT * from employe WHERE salaire > 3000;")

print(f"Employés dont le salaire dépasse 3000€: {mycursor.fetchall()}")

mycursor.execute("SELECT service.nom, employe.nom, employe.prenom, employe.salaire FROM employe INNER JOIN service ON service.id = employe.id_service")

for employe in mycursor:
    print(f"{employe[2]} {employe[1]} travaille au service {employe[0]} et touche {employe[3]}€ par mois.")

employe1 = Employe()
employe1.read(1)
print(f"{employe1.get_prenom()} {employe1.get_nom()} instancié avec la méthode Employe.read()")

employe4 = Employe()
employe4.create("GEORGET","Arthur",4340,1)
print(f"{employe4.get_prenom()} {employe4.get_nom()} instancié avec la méthode Employe.create() et ajouté à la table employe a l'id {employe4.get_id()}.")


mycursor.execute("SELECT service.nom, employe.nom, employe.prenom, employe.salaire FROM employe INNER JOIN service ON service.id = employe.id_service")

for employe in mycursor:
    print(f"{employe[2]} {employe[1]} travaille au service {employe[0]} et touche {employe[3]}€ par mois.")


print("Suppression de l'employe4.")

employe4.delete()

mycursor.execute("SELECT service.nom, employe.nom, employe.prenom, employe.salaire FROM employe INNER JOIN service ON service.id = employe.id_service")

for employe in mycursor:
    print(f"{employe[2]} {employe[1]} travaille au service {employe[0]} et touche {employe[3]}€ par mois.")

mycursor.close()
mydb.close()