from DataBase import DataBase


class Product:

    def __init__(self, database: DataBase):

        self.__database_connection = database.connection
        self.__id = None
        self.__name = None
        self.__description = None
        self.__price = None
        self.__quantity = None
        self.__id_category = None


    def get_id(self):

        return self.__id


    def get_name(self):

        return self.__name


    def get_description(self):

        return self.__description


    def get_price(self):

        return self.__price


    def get_quantity(self):

        return self.__quantity


    def get_id_category(self):

        return self.__id_category


    def create(self, name: str, description: str, price: float, quantity: int ,id_category: int):

        local_cursor = self.__database_connection.cursor()
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity
        self.__id_category = id_category
        local_cursor.execute(f"INSERT INTO product (name, description, price, quantity, id_category) VALUES ('{self.__name}', '{self.__description}', {self.__price}, {self.__quantity}, {self.__id_category})")
        self.__id = local_cursor.lastrowid
        self.__database_connection.commit()
        local_cursor.close()


    def read(self, id: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"SELECT * from product WHERE id = {id};")
        result = local_cursor.fetchall()
        print(result)
        self.__id = id
        self.__name = result[0][1]
        self.__description = result[0][2]
        self.__price = result[0][3]
        self.__quantity = result[0][4]
        self.__id_category = result[0][5]
        local_cursor.close()


    def update_name(self, name: str):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE product SET name = '{name}' WHERE id = {self.__id};")
        self.__name = name
        local_cursor.close()


    def update_description(self, description: str):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE product SET description = '{description}' WHERE id = {self.__id};")
        self.__description = description
        local_cursor.close()


    def update_price(self, price: int):

        local_cursor = self.__database_connection.cursor()
        local_cursor.execute(f"UPDATE product SET price = {price} WHERE id = {self.__id};")
        self.__price = price
        local_cursor.close()


    def update_id_category(self, id_category: int):

        local_cursor = self.__database_connection.cursor()        
        local_cursor.execute(f"UPDATE product SET id_category = {id_category} WHERE id = {self.__id};")
        self.__id_category = id_category
        local_cursor.close()


    def update_quantity(self, quantity: int):

        local_cursor = self.__database_connection.cursor()  
        local_cursor.execute(f"UPDATE product SET quantity = {quantity} WHERE id = {self.__id};")
        self.__quantity = quantity
        local_cursor.close()


    def delete(self, id: int = None):

        local_cursor = self.__database_connection.cursor()  
        if not id:
            id = self.__id
        local_cursor.execute(f"DELETE FROM product WHERE id = {id}")
        self.__database_connection.commit()
        local_cursor.close()
