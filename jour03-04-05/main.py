from src.DataBase import DataBase
from src.Menu import Menu

def main():

    database = DataBase()
    database.init_store()
    menu = Menu(database)
    menu.main_menu()
    database.connection.close()

if __name__ == "__main__":
    main()