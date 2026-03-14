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

        self.protocol("WM_DELETE_WINDOW", self.__close_database_n_quit_application)

        self.__database.init_store()

        self.columnconfigure(0, weight=50)
        self.columnconfigure(1, weight=80)
        self.columnconfigure(2, weight=80)
        self.columnconfigure(3, weight=80)
        self.columnconfigure(4, weight=80)
        self.columnconfigure(5, weight=80)
        self.columnconfigure(6, weight=80)
        self.columnconfigure(7, weight=80)

        self.__instantiate_categories()

        self.__categories_filter_frame = CategoriesFilterFrame(self, self.__categories, title="Filtrer", width=100, height=35)
        self.__categories_filter_frame.grid(row=0, column=1, sticky="W", pady=5)

        self.selected_category_id = None

        self.__instantiate_products()

        self.__products_frame = ProductsFrame(self, self.__products, title="Produits en stock", width=500)
        self.__products_frame.grid(row=1, column=1, columnspan=5, sticky="W", pady=5)

        add_product_button = customtkinter.CTkButton(self, text="Ajouter produit", command=self.__call_add_product_window)
        add_product_button.grid(row=2, column=1, sticky="W", pady=5, padx=5)

        self.__categories_frame = CategoriesFrame(self, self.__categories, title="Catégories", width=150)
        self.__categories_frame.grid(row=1, column=7, columnspan=3, sticky="E", pady=5, padx=10)
        
        add_category_button = customtkinter.CTkButton(self, text="Ajouter catégorie", command=self.__call_add_category_window)
        add_category_button.grid(row=2, column=5, columnspan=3, sticky="E", pady=5, padx=10)

        self.bind('<FocusIn>',self.reinstantiate_frames)


    def __instantiate_products(self) -> list[Product]:

        local_cursor = self.__database.connection.cursor()

        local_cursor.execute("USE store;")

        self.__selected_category_id = self.__categories_filter_frame.get_selected_id()
        
        if self.__selected_category_id is not None:
            local_cursor.execute(f"SELECT id FROM product WHERE id_category = {self.__selected_category_id};")
        else:
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


    def __close_database_n_quit_application(self):

        self.__database.connection.close()
        self.destroy()

    
    def reinstantiate_frames(self,event):

        if event is None or event.widget == event.widget.winfo_toplevel():

            self.__instantiate_products()
            self.__products_frame = ProductsFrame(self, self.__products, title="Produits en stock", width=500)
            self.__products_frame.grid(row=1, column=1, columnspan=5, sticky="W", pady=5)

            self.__instantiate_categories()
            self.__categories_frame = CategoriesFrame(self, self.__categories, title="Catégories", width=150)
            self.__categories_frame.grid(row=1, column=7, columnspan=3, sticky="E", pady=5, padx=10)