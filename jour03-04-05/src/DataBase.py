import mysql.connector
from Category import Category
from Product import Product

class DataBase:
    
    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            port="33059",
            user="arthur",
            password="marth19"
            )
        print(self.connection)


    def init_store(self):

        local_cursor = self.connection.cursor()
        local_cursor.execute("CREATE DATABASE store;")
        local_cursor.execute("USE store;")
        local_cursor.execute("CREATE TABLE category (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255));")
        local_cursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), description VARCHAR, price INT, quantity INT, id_category INT NOT NULL, PRIMARY KEY(id), FOREIGN KEY (id_category) REFERENCES category(id));")
        self.connection.commit()
        local_cursor.close()

    
    def instantiate_product(self) -> list[Product]:

        local_cursor = self.connection.cursor()
        local_cursor.execute("USE store;")
        local_cursor.execute("SELECT id FROM product;")
        products = local_cursor.fetchall()
        products_instance_list = []
        for product in products:
            product_instance = Product(self)
            product_instance.read(product[0])
            products_instance_list.append(product_instance)
        local_cursor.close()
        return products_instance_list


    def instantiate_category(self) -> list[Category]:

        local_cursor = self.connection.cursor()
        local_cursor.execute("USE zoo;")
        local_cursor.execute("SELECT id FROM category;")
        categories = local_cursor.fetchall()
        categories_instance_list = []
        for category in categories:
            category_instance = Category(self)
            category_instance.read(category[0])
            categories_instance_list.append(category_instance)
        local_cursor.close()
        return categories_instance_list