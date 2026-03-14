import mysql.connector


class DataBase:
    
    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="user",
            password="password"
            )
        print(self.connection)


    def init_store(self):

        local_cursor = self.connection.cursor()
        try:
            local_cursor.execute("CREATE DATABASE store;")
            print("'store' database created.")
        except:
            print("'store' database found.")
        local_cursor.execute("USE store;")
        try:
            local_cursor.execute("CREATE TABLE category (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255));")
            print("'category' table created.")
        except:
            print("'category' table found.")
        try:
            local_cursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), description VARCHAR(255), price INT, quantity INT, id_category INT NOT NULL, PRIMARY KEY(id), FOREIGN KEY (id_category) REFERENCES category(id) ON DELETE CASCADE);")
            print("'product' table created.")
        except:
            print("'product' table found.")
        self.connection.commit()
        local_cursor.close()