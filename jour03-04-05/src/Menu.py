from src.DataBase import DataBase
from src.Category import Category
from src.Product import Product


class Menu:

    def __init__(self, database: DataBase):
        self.__database = database
        self.__products = database.instantiate_product()
        self.__categories = database.instantiate_category()
        print("Bienvenue dans l'interface d'administration du magasin.")
    

    def main_menu(self):

        while True:

            print('''
-------- Menu principal --------
Que voulez vous faire?
1 - Gérer les produits
2 - Gérer les categories
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
                    self.__product_menu()
                case 2:
                    self.__category_menu()
                case 3:
                    return


    def __product_menu(self):

        print('''
-------- Gestion des produits --------
Que voulez vous faire?
0 - Retour
1 - Ajouter un produit
2 - Supprimer un produit
3 - Modifier un produit
4 - Afficher l'ensemble des produits
              
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
                self.__product_add_menu()
                return
            case 2:
                self.__product_remove_menu()
                return
            case 3:
                self.__product_modify_menu()
                return
            case 4:
                self.__print_all_products_infos()
                return


    def __product_add_menu(self):

        if len(self.__categories) < 1:
            print("Vous ne pouvez pas ajouter de produit, vous n'avez pas de categorie.")
        else:
            print('''-------- Ajouter un produit --------''')
            name = input("Veuillez renseigner un nom: ")
            description = input("Veuillez renseigner une description: ")
            self.__print_available_categories_ids()
            while True:
                user_input = input("Veuillez renseigner un id de categorie: ")
                try:
                    id_category_type = int(user_input)
                    break
                except:
                    print("Vous n'avez pas renseigné un chiffre.")
            while True:
                user_input = input("Veuillez renseigner un prix: ")
                try:
                    price = int(user_input)
                    break
                except:
                    print("Vous n'avez pas renseigné un chiffre.")
            while True:
                user_input = input("Veuillez renseigner une quantité: ")
                try:
                    quantity = int(user_input)
                    break
                except:
                    print("Vous n'avez pas renseigné un chiffre.")
            product = Product(self.__database)
            product.create(name, description, price, quantity, id_category_type)
            self.__products.append(product)


    def __product_remove_menu(self):
        
        print('''
-------- Supprimer un produit --------''')
        self.__print_available_products_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id du produit à supprimer: ")
            try:
                id_product = int(user_input)
                for product in self.__products:
                    if product.get_id() == id_product:
                        product.delete()
                        self.__products.remove(product)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")
        

    def __product_modify_menu(self):
        
        print('''
-------- Modifier un product --------''')
        self.__print_available_products_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id du produit à modifier: ")
            try:
                id_product = int(user_input)
                id_found = False
                for product in self.__products:
                    if product.get_id() == id_product:
                        self.__product_modify_submenu(product)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")


    def __product_modify_submenu(self, product: Product):

        print(f'''
-------- Modifier {product.get_name()} --------
description: {product.get_description()}
categorie n°: {product.get_id_category()}
Prix: {product.get_price()}
Quantité : {product.get_quantity()} 

Que voulez vous faire?
0 - Retour
1 - Modifier son nom
2 - Modifier sa description
3 - Modifier sa categorie
4 - Modifier son prix
5 - Modifier sa quantité
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
                product.update_name(input("Veuillez renseigner son nouveau nom: "))
            case 2:
                product.update_description(input("Veuillez renseigner sa nouvelle description: "))
            case 3:
                while True:
                    user_input = input("Veuillez renseigner l'id de sa nouvelle categorie: ")
                    try:
                        id_category = int(user_input)
                        break
                    except:
                        print("Vous n'avez pas renseigné un chiffre.")
                product.update_id_category(id_category)
            case 4:
                while True:
                    user_input = input("Veuillez renseigner son nouveau prix: ")
                    try:
                        product.update_price(int(user_input))
                        break
                    except:
                        print("Vous n'avez pas renseigné un chiffre.")
            case 5:
                while True:
                    user_input = input("Veuillez renseigner sa nouvelle quantité: ")
                    try:
                        product.update_quantity(int(user_input))
                        break
                    except:
                        print("Vous n'avez pas renseigné un chiffre.")


    def __category_menu(self):
        print('''
-------- Gestion des categories --------
Que voulez vous faire?
0 - Retour
1 - Ajouter une categorie
2 - Supprimer une categorie
3 - Modifier une categorie
4 - Afficher les produits par categorie

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
                self.__category_add_menu()
                return
            case 2:
                self.__category_remove_menu()
                return
            case 3:
                self.__category_modify_menu()
                return
            case 4:
                self.__category_products_menu()
                return


    def __category_add_menu(self):

        print('''
-------- Ajouter une categorie --------
''')
        name = input("Veuillez renseigner un nom: ")
        category = Category(self.__database)
        category.create(name)
        self.__categories.append(category)


    def __category_remove_menu(self):

        print('''
-------- Supprimer une categorie --------
''')
        self.__print_available_categories_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id de la categorie à supprimer: ")
            try:
                id_category = int(user_input)
                for category in self.__categories:
                    if category.get_id() == id_category:
                        category.delete()
                        self.__categories.remove(category)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")


    def __category_modify_menu(self):
        
        print('''
-------- Modifier une categorie --------
''')
        self.__print_available_categories_ids()
        id_found = False
        while not id_found:
            user_input = input("Veuillez renseigner l'id de la categorie à modifier: ")
            try:
                id_category = int(user_input)
                id_found = False
                for category in self.__categories:
                    if category.get_id() == id_category:
                        self.__category_modify_submenu(category)
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")


    def __category_modify_submenu(self, category: Category):

        print(f'''
-------- Modifier la categorie n°{category.get_id()} --------

Nom: {category.get_name()}

Que voulez vous faire?
0 - Retour
1 - Modifier son nom

''')
        while True:
            user_input = input("Veuillez sélectionner une option (0-1): ")
            try:
                choice = int(user_input)
                if 0 <= choice <= 1:
                    break
                else:
                    print("Cette option n'est pas disponible.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")

        match choice:
            case 0:
                pass
            case 1:    
                category.update_name(input("Veuillez renseigner son nouveau nom: "))     


    def __category_products_menu(self):

        print('''
-------- Produits par categorie --------
              ''')
        self.__print_available_categories_ids()
        id_found = False
        while not id_found:
            user_input = input("De quelle categorie voulez-vous lister tous les produits?: ")
            try:
                id_category = int(user_input)
                id_found = False
                for category in self.__categories:
                    if category.get_id() == id_category:
                        category.print_products_infos_by_category()
                        id_found = True
                if not id_found:
                    print("L'id renseigné n'existe pas.")
            except:
                print("Vous n'avez pas renseigné un chiffre.")
    

    def __print_available_categories_ids(self):

        categories_ids_str = ""
        for category in self.__categories:
            categories_ids_str += f"{category.get_id()} "
        print(f"Categories disponibles: {categories_ids_str[:-1]}")


    def __print_available_products_ids(self):

        products_ids_str = ""
        for product in self.__products:
            products_ids_str += f"{product.get_id()} "
        print(f"Produits disponibles: {products_ids_str[:-1]}")


    def __print_all_products_infos(self):
        for product in self.__products:
            print(f'''
=============================================
Id: {product.get_id()}
Nom: {product.get_name()}
Description: {product.get_description()}
Prix: {product.get_price()}
Quantité: {product.get_quantity()}
=============================================               
''')