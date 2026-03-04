import mysql.connector
from sys import exit


class DataBase:
    
    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="youruser",
            password="yourpassword"
            )
        print(self.connection)


    def init_zoo(self):

        local_cursor = self.connection.cursor()
        local_cursor.execute("CREATE DATABASE zoo;")
        local_cursor.execute("USE zoo;")
        local_cursor.execute("CREATE TABLE cage (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, size INT, capacity INT);")
        local_cursor.execute("CREATE TABLE animal (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(63), race VARCHAR(63), birthdate VARCHAR(15), origin_country VARCHAR(63), id_cage_type INT NOT NULL, PRIMARY KEY(id), FOREIGN KEY (id_cage_type) REFERENCES cage(id));")
        self.connection.commit()
        local_cursor.close()

    
    def instantiate_animals(self):

        local_cursor = self.connection.cursor()
        local_cursor.execute("USE zoo;")
        local_cursor.execute("SELECT id FROM animal;")
        animals = local_cursor.fetchall()
        animals_instance_list = []
        for animal in animals:
            animal_instance = Animal(self)
            animal_instance.read(animal[0])
            animals_instance_list.append(animal_instance)
        local_cursor.close()
        return animals_instance_list


    def instantiate_cages(self):

        local_cursor = self.connection.cursor()
        local_cursor.execute("USE zoo;")
        local_cursor.execute("SELECT id FROM cage;")
        cages = local_cursor.fetchall()
        cages_instance_list = []
        for cage in cages:
            cage_instance = Cage(self)
            cage_instance.read(cage[0])
            cages_instance_list.append(cage_instance)
        local_cursor.close()
        return cages_instance_list


class Cage:

    def __init__(self, database: DataBase):

        self.__database_connection = database.connection
        self.__id = None
        self.__size = None
        self.__capacity = None


    def get_id(self):

        return self.__id
    

    def get_size(self):

        return self.__size
    

    def get_capacity(self):

        return self.__capacity
    

    def create(self, size: str, capacity: int):

        local_cursor = self.__database_connection.cursor()
        self.__size = size
        self.__capacity = capacity
        local_cursor.execute(f"INSERT INTO cage (size, capacity) VALUES ('{self.__size}', '{self.__capacity}')")
        self.__id = local_cursor.lastrowid
        self.__database_connection.commit()
        local_cursor.close()


    def read(self, id: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"SELECT * from cage WHERE id = {id}")
        result = local_cursor.fetchall()
        self.__id = id
        self.__size = result[0][1]
        self.__capacity = result[0][2]
        local_cursor.close()


    def update_size(self, size: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE cage SET size = {size} WHERE id = {self.__id};")
        self.__size = size
        local_cursor.close()


    def update_capacity(self, capacity: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE cage SET capacity = {capacity} WHERE id = {self.__id};")
        self.__capacity = capacity
        local_cursor.close()


    def delete(self, id: int = None):

        local_cursor = self.__database_connection.cursor()
        if not id:
            id = self.__id
        local_cursor.execute(f"DELETE FROM cage WHERE id = {id}")
        self.__database_connection.commit()
        local_cursor.close()


    def print_animals_infos_by_cage(self):
        
        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"SELECT * FROM animal WHERE id_cage_type = {self.__id};")
        print(f"Dans la cage n° {self.__id} il y a:")
        for animal in local_cursor:
            print(f'''
=============================================
Id: {animal[0]}
Nom: {animal[1]}
Race: {animal[2]}
Date de naissance: {animal[3]}
Pays d'origine: {animal[4]}
=============================================               
''')
        
        local_cursor.close()


class Animal:

    def __init__(self, database: DataBase):

        self.__database_connection = database.connection
        self.__id = None
        self.__name = None
        self.__race = None
        self.__birthdate = None
        self.__origin_country = None
        self.__id_cage_type = None


    def get_id(self):

        return self.__id


    def get_name(self):

        return self.__name


    def get_race(self):

        return self.__race


    def get_birthdate(self):

        return self.__birthdate


    def get_origin_country(self):

        return self.__origin_country


    def get_id_cage_type(self):

        return self.__id_cage_type


    def create(self, name: str, race: str, birthdate: str, origin_country: str ,id_cage_type: int):

        local_cursor = self.__database_connection.cursor()
        self.__name = name
        self.__race = race
        self.__birthdate = birthdate
        self.__origin_country = origin_country
        self.__id_cage_type = id_cage_type
        local_cursor.execute(f"INSERT INTO animal (name, race, birthdate, origin_country, id_cage_type) VALUES ('{self.__name}', '{self.__race}', '{self.__birthdate}', '{self.__origin_country}', {self.__id_cage_type})")
        self.__id = local_cursor.lastrowid
        self.__database_connection.commit()
        local_cursor.close()


    def read(self, id: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"SELECT * from animal WHERE id = {id};")
        result = local_cursor.fetchall()
        print(result)
        self.__id = id
        self.__name = result[0][1]
        self.__race = result[0][2]
        self.__birthdate = result[0][3]
        self.__origin_country = result[0][4]
        self.__id_cage_type = result[0][5]
        local_cursor.close()


    def update_name(self, name: str):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE animal SET name = '{name}' WHERE id = {self.__id};")
        self.__name = name
        local_cursor.close()


    def update_race(self, race: str):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE animal SET race = '{race}' WHERE id = {self.__id};")
        self.__race = race
        local_cursor.close()


    def update_birthdate(self, birthdate: float):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE animal SET birthdate = '{birthdate}' WHERE id = {self.__id};")
        self.__birthdate = birthdate
        local_cursor.close()


    def update_id_cage_type(self, id_cage_type: int):

        local_cursor = self.__database_connection.cursor()        
        local_cursor.execute(f"UPDATE animal SET id_cage_type = {id_cage_type} WHERE id = {self.__id};")
        self.__id_cage_type = id_cage_type
        local_cursor.close()


    def update_origin_country(self, origin_country: str):

        local_cursor = self.__database_connection.cursor()  
        local_cursor.execute(f"UPDATE animal SET origin_country = '{origin_country}' WHERE id = {self.__id};")
        self.__origin_country = origin_country
        local_cursor.close()


    def delete(self, id: int = None):

        local_cursor = self.__database_connection.cursor()  
        if not id:
            id = self.__id
        local_cursor.execute(f"DELETE FROM animal WHERE id = {id}")
        self.__database_connection.commit()
        local_cursor.close()


class Menu:

    def __init__(self, database: DataBase):
        self.__database = database
        self.__animals = database.instantiate_animals()
        self.__cages = database.instantiate_cages()
        print("Bienvenue dans l'interface d'administration du zoo.")
    

    def main_menu(self):

        while True:

            print('''
-------- Menu principal --------
Que voulez vous faire?
1 - Gérer les animaux
2 - Gérer les cages
3 - Quitter''')
        
            while True:
                user_input = input("Veuillez sélectionner une option (1-3): ")
                try:
                    choice = int(user_input)
                    if 1 <= choice <= 3:
                        break
                    else:
                        print("Cette option n'est pas disponible à ce niveau.")
                except:
                    print("Vous n'avez pas renseigné un chiffre.")

            match choice:
                case 1:
                    self.__animal_menu()
                case 2:
                    self.__cage_menu()
                case 3:
                    return


    def __animal_menu(self):

        print('''
-------- Gestion des animaux --------
Que voulez vous faire?
0 - Retour
1 - Ajouter un animal
2 - Supprimer un animal
3 - Modifier un animal
4 - Afficher l'ensemble des animaux
              
''')
        while True:
            user_input = input("Veuillez sélectionner une option (0-4): ")
            try:
                choice = int(user_input)
                if 0 <= choice <= 4:
                    break
                else:
                    print("Cette option n'est pas disponible à ce niveau.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")

        match choice:
            case 0:
                return
            case 1:
                self.__animal_add_menu()
                return
            case 2:
                self.__animal_remove_menu()
                return
            case 3:
                self.__animal_modify_menu()
                return
            case 4:
                self.__print_all_animals_infos()
                return


    def __animal_add_menu(self):

        if len(self.__cages) < 1:
            print("Vous ne pouvez pas ajouter d'animal, vous n'avez pas de cage.")
        else:
            print('''-------- Ajouter un animal --------''')
            name = input("Veuillez renseigner un nom: ")
            race = input("Veuillez renseigner une race: ")
            self.__print_available_cages_ids()
            while True:
                user_input = input("Veuillez renseigner un id de cage: ")
                try:
                    id_cage_type = int(user_input)
                    break
                except:
                    print("Vous n'avez pas renseigné un chiffre.")
            birthdate = input("Veuillez renseigner une date de naissance: ")
            origin_country = input("Veuillez renseigner un pays d'origine: ")
            animal = Animal(self.__database)
            animal.create(name, race, birthdate, origin_country, id_cage_type)
            self.__animals.append(animal)


    def __animal_remove_menu(self):
        
        print('''
-------- Supprimer un animal --------''')
        self.__print_available_animals_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id de l'animal à supprimer: ")
            try:
                id_animal = int(user_input)
                for animal in self.__animals:
                    if animal.get_id() == id_animal:
                        animal.delete()
                        self.__animals.remove(animal)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")
        

    def __animal_modify_menu(self):
        
        print('''
-------- Modifier un animal --------''')
        self.__print_available_animals_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id de l'animal à modifier: ")
            try:
                id_animal = int(user_input)
                id_found = False
                for animal in self.__animals:
                    if animal.get_id() == id_animal:
                        self.__animal_modify_submenu(animal)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")


    def __animal_modify_submenu(self, animal: Animal):

        print(f'''
-------- Modifier {animal.get_name()} --------
Race: {animal.get_race()}
Cage n°: {animal.get_id_cage_type()}
Date de naissance: {animal.get_birthdate()}
Pays d'origine : {animal.get_origin_country()} 

Que voulez vous faire?
0 - Retour
1 - Modifier son nom
2 - Modifier sa race
3 - Modifier sa cage
4 - Modifier sa date de naissance
5 - Modifier son pays d'origine
''')
        while True:
            user_input = input("Veuillez sélectionner une option (0-5): ")
            try:
                choice = int(user_input)
                if 0 <= choice <= 5:
                    break
                else:
                    print("Cette option n'est pas disponible.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")

        match choice:
            case 0:
                pass
            case 1:
                animal.update_name(input("Veuillez renseigner son nouveau nom: "))
            case 2:
                animal.update_race(input("Veuillez renseigner sa nouvelle race: "))
            case 3:
                while True:
                    user_input = input("Veuillez renseigner l'id de sa nouvelle cage: ")
                    try:
                        id_cage_type = int(user_input)
                        break
                    except:
                        print("Vous n'avez pas renseigné un chiffre.")
                animal.update_id_cage_type(id_cage_type)
            case 4:
                animal.update_birthdate(input("Veuillez renseigner sa nouvelle date de naissance: "))
            case 5:
                animal.update_origin_country(input("Veuillez renseigner son nouveau pays d'origine: "))


    def __cage_menu(self):
        print('''
-------- Gestion des cages --------
Que voulez vous faire?
0 - Retour
1 - Ajouter une cage
2 - Supprimer une cage
3 - Modifier une cage
4 - Afficher les animaux par cage

''')
        while True:
            user_input = input("Veuillez sélectionner une option (0-4): ")
            try:
                choice = int(user_input)
                if 0 <= choice <= 4:
                    break
                else:
                    print("Cette option n'est pas disponible à ce niveau.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")

        match choice:
            case 0:
                pass
            case 1:
                self.__cage_add_menu()
                return
            case 2:
                self.__cage_remove_menu()
                return
            case 3:
                self.__cage_modify_menu()
                return
            case 4:
                self.__cage_animals_menu()
                return


    def __cage_add_menu(self):

        print('''
-------- Ajouter une cage --------
''')
        size = input("Veuillez renseigner une superficie: ")
        capacity = input("Veuillez renseigner une capacité: ")
        cage = Cage(self.__database)
        cage.create(size, capacity)
        self.__cages.append(cage)


    def __cage_remove_menu(self):

        print('''
-------- Supprimer une cage --------
''')
        self.__print_available_cages_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id de la cage à supprimer: ")
            try:
                id_cage = int(user_input)
                for cage in self.__cages:
                    if cage.get_id() == id_cage:
                        cage.delete()
                        self.__cages.remove(cage)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")


    def __cage_modify_menu(self):
        
        print('''
-------- Modifier une cage --------
''')
        self.__print_available_cages_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id de la cage à modifier: ")
            try:
                id_cage = int(user_input)
                id_found = False
                for cage in self.__cages:
                    if cage.get_id() == id_cage:
                        self.__cage_modify_submenu(cage)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")


    def __cage_modify_submenu(self, cage: Cage):

        print(f'''
-------- Modifier la cage n°{cage.get_id()} --------

Surface: {cage.get_size()}
Capacité: {cage.get_capacity()}

Que voulez vous faire?
0 - Retour
1 - Modifier sa surface
2 - Modifier sa capacité

''')
        while True:
            user_input = input("Veuillez sélectionner une option (0-2): ")
            try:
                choice = int(user_input)
                if 0 <= choice <= 2:
                    break
                else:
                    print("Cette option n'est pas disponible.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")

        match choice:
            case 0:
                pass
            case 1:
                while True:
                    user_input = input("Veuillez renseigner sa nouvelle taille: ")
                    
                    size = int(user_input)
                    break
                    
                cage.update_size(size)
            case 2:
                while True:
                    user_input = input("Veuillez renseigner sa nouvelle capacité: ")
                    try:
                        capacity = int(user_input)
                        break
                    except:
                        print("Vous n'avez pas renseigné un chiffre.")
                cage.update_capacity(capacity)      


    def __cage_animals_menu(self):

        print('''
-------- Animaux par cage --------
              ''')
        self.__print_available_cages_ids()
        id_found = False
        while not id_found:
            user_input = input("De quelle cage voulez-vous lister tous les animaux?: ")
            try:
                id_cage = int(user_input)
                id_found = False
                for cage in self.__cages:
                    if cage.get_id() == id_cage:
                        cage.print_animals_infos_by_cage()
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")
    

    def __print_available_cages_ids(self):

        cages_ids_str = ""
        for cage in self.__cages:
            cages_ids_str += f"{cage.get_id()} "
        print(f"Cages disponibles: {cages_ids_str[:-1]}")


    def __print_available_animals_ids(self):

        animals_ids_str = ""
        for animal in self.__animals:
            animals_ids_str += f"{animal.get_id()} "
        print(f"Animaux disponibles: {animals_ids_str[:-1]}")


    def __print_all_animals_infos(self):
        for animal in self.__animals:
            print(f'''
=============================================
Id: {animal.get_id()}
Nom: {animal.get_name()}
Race: {animal.get_race()}
Date de naissance: {animal.get_birthdate()}
Pays d'origine: {animal.get_origin_country()}
=============================================               
''')


def main():

    database = DataBase()
    database.init_zoo()
    menu = Menu(database)
    menu.main_menu()
    database.connection.close()

if __name__ == "__main__":
    main()