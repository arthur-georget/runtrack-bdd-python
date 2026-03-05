from DataBase import DataBase


class Category:

    def __init__(self, database: DataBase):

        self.__database_connection = database.connection
        self.__id = None
        self.__name = None


    def get_id(self):

        return self.__id
    

    def get_name(self):

        return self.__name
    

    def create(self, name: str):

        local_cursor = self.__database_connection.cursor()
        self.__name = name
        local_cursor.execute(f"INSERT INTO category (name) VALUES ('{self.__name}')")
        self.__id = local_cursor.lastrowid
        self.__database_connection.commit()
        local_cursor.close()


    def read(self, id: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"SELECT * from category WHERE id = {id}")
        result = local_cursor.fetchall()
        self.__id = id
        self.__name = result[0][1]
        local_cursor.close()


    def update_name(self, name: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE category SET name = {name} WHERE id = {self.__id};")
        self.__name = name
        local_cursor.close()


    def delete(self, id: int = None):

        local_cursor = self.__database_connection.cursor()
        if not id:
            id = self.__id
        local_cursor.execute(f"DELETE FROM category WHERE id = {id}")
        self.__database_connection.commit()
        local_cursor.close()


    def print_products_infos_by_category(self):
        
        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"SELECT * FROM product WHERE id_category_type = {self.__id};")
        print(f"Dans la category n° {self.__id} il y a:")
        for product in local_cursor:
            print(f'''
=============================================
Id: {product[0]}
Nom: {product[1]}
Description: {product[2]}
Prix: {product[3]}
Quantité: {product[4]}
=============================================               
''')
        
        local_cursor.close()