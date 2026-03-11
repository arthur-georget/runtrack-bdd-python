from src.model.DataBase import DataBase
from src.model.Category import Category
from src.model.Product import Product
from src.view.frames.ProductsFrame import ProductsFrame
from src.view.frames.CategoriesFilterFrame import CategoriesFilterFrame
from src.view.windows.AddProductInputDialog import AddProductInputDialog
from functools import partial
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    def __init__(self, *args, **kwargs):

        customtkinter.CTk.__init__(self, *args, **kwargs)

        self.title("Gestionnaire de stock")
        self.geometry("800x600")
        self.__database = DataBase()

        ########## CLOSE DATABASE WHEN EXITING ###########
        self.protocol("WM_DELETE_WINDOW", self.__database.connection.close())

        self.__database = DataBase()
        self.__database.init_store()
        self.__instantiate_products()
        self.__instantiate_categories()

        ########## CTk FRAMES #############
        self.columnconfigure(0, weight=50)
        self.columnconfigure(1, weight=80)
        self.columnconfigure(2, weight=80)
        self.columnconfigure(3, weight=80)
        self.columnconfigure(4, weight=80)
        self.columnconfigure(5, weight=80)
        self.columnconfigure(6, weight=80)
        self.columnconfigure(7, weight=80)

        categories_filter_frame = CategoriesFilterFrame(self, title="Filtrer", width=100, height=35)
        categories_filter_frame.grid(row=0, column=1, sticky="W", pady=5)

        self.__products_frame = ProductsFrame(self, self.__products, title="Produits en stock", width=500)
        self.__products_frame.grid(row=1, column=1, columnspan=5, sticky="W", pady=5)
        self.bind('<FocusIn>',self.__instantiate_product_frame)

        add_product_button = customtkinter.CTkButton(self, text="Ajouter", command=self.__call_add_product_window)
        add_product_button.grid(row=2, column=1, sticky="W", pady=5, padx=5)

    def get_products(self):
        return self.__products
    
    def get_categories(self):
        return self.__categories

    def __instantiate_products(self) -> list[Product]:

        self.__database.connection
        local_cursor = self.__database.connection.cursor()
        local_cursor.execute("USE store;")
        local_cursor.execute("SELECT id FROM product;")
        products = local_cursor.fetchall()
        products_instance_list = []
        for product in products:
            product_instance = Product(self.__database)
            product_instance.read(product[0])
            products_instance_list.append(product_instance)
        local_cursor.close()
        self.__products =  products_instance_list


    def __instantiate_categories(self) -> list[Category]:

        local_cursor = self.__database.connection.cursor()
        local_cursor.execute("USE store;")
        local_cursor.execute("SELECT id FROM category;")
        categories = local_cursor.fetchall()
        categories_instance_list = []
        for category in categories:
            category_instance = Category(self.__database)
            category_instance.read(category[0])
            categories_instance_list.append(category_instance)
        local_cursor.close()
        self.__categories = categories_instance_list

    def __call_add_product_window(self):
        self.__add_product_window = AddProductInputDialog(self, database = self.__database)
        self.__add_product_window.bind('<Destroy>',self.__instantiate_product_frame)

    def __instantiate_product_frame(self,event):
        if event.widget == event.widget.winfo_toplevel():
            print("Instantiating ProductFrame")
            self.__instantiate_products()
            self.__products_frame = ProductsFrame(self, self.__products, title="Produits en stock", width=500)
            self.__products_frame.grid(row=1, column=1, columnspan=5, sticky="W", pady=5)