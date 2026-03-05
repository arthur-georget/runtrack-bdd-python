import mysql.connector


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
        try:
            local_cursor.execute("CREATE DATABASE store;")
            print("Base de donnée 'store' créée.")
        except:
            print("Base de donnée 'store' trouvée.")
        local_cursor.execute("USE store;")
        try:
            local_cursor.execute("CREATE TABLE category (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255));")
            print("La table 'category' a été créée.")
        except:
            print("Table 'category' trouvée.")
        try:
            local_cursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), description VARCHAR(255), price INT, quantity INT, id_category INT NOT NULL, PRIMARY KEY(id), FOREIGN KEY (id_category) REFERENCES category(id));")
            print("La table 'product a été créée.'")
        except:
            print("Table 'product' trouvée.")
        self.connection.commit()
        local_cursor.close()