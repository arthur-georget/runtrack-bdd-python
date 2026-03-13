from src.model.DataBase import DataBase
from src.model.Category import Category
from src.model.Product import Product
from src.view.frames.ProductsFrame import ProductsFrame
from src.view.frames.CategoriesFrame import CategoriesFrame
from src.view.frames.CategoriesFilterFrame import CategoriesFilterFrame
from src.view.windows.AddProductInputDialog import AddProductInputDialog
from src.view.windows.AddCategoryInputDialog import AddCategoryInputDialog
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

        self.columnconfigure(0, weight=50)
        self.columnconfigure(1, weight=80)
        self.columnconfigure(2, weight=80)
        self.columnconfigure(3, weight=80)
        self.columnconfigure(4, weight=80)
        self.columnconfigure(5, weight=80)
        self.columnconfigure(6, weight=80)
        self.columnconfigure(7, weight=80)

        categories_filter_frame = CategoriesFilterFrame(self, self.__categories, title="Filtrer", width=100, height=35)
        categories_filter_frame.grid(row=0, column=1, sticky="W", pady=5)

        self.__products_frame = ProductsFrame(self, self.__products, title="Produits en stock", width=500)
        self.__products_frame.grid(row=1, column=1, columnspan=5, sticky="W", pady=5)

        add_product_button = customtkinter.CTkButton(self, text="Ajouter produit", command=self.__call_add_product_window)
        add_product_button.grid(row=2, column=1, sticky="W", pady=5, padx=5)

        self.__categories_frame = CategoriesFrame(self, self.__categories, title="Catégories", width=150)
        self.__categories_frame.grid(row=1, column=7, columnspan=3, sticky="E", pady=5, padx=10)
        
        add_category_button = customtkinter.CTkButton(self, text="Ajouter catégorie", command=self.__call_add_category_window)
        add_category_button.grid(row=2, column=5, columnspan=3, sticky="E", pady=5, padx=10)

        self.bind('<FocusIn>',self.__reinstantiate_frames)


    def get_products(self):

        return self.__products
    

    def get_categories(self):

        return self.__categories


    def __instantiate_products(self) -> list[Product]:

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

        AddProductInputDialog(self, database = self.__database)

    
    def __call_add_category_window(self):

        AddCategoryInputDialog(self, database = self.__database)


    def __reinstantiate_frames(self,event):

        if event.widget == event.widget.winfo_toplevel():
            print("Instantiating main window frames")
            
            self.__instantiate_products()
            self.__products_frame = ProductsFrame(self, self.__products, title="Produits en stock", width=500)
            self.__products_frame.grid(row=1, column=1, columnspan=5, sticky="W", pady=5)

            self.__instantiate_categories()
            self.__categories_frame = CategoriesFrame(self, self.__categories, title="Catégories", width=150)
            self.__categories_frame.grid(row=1, column=7, columnspan=3, sticky="E", pady=5, padx=10)