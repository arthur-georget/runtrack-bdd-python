import customtkinter
from src.model.Product import Product

class AddProductInputDialog(customtkinter.CTkToplevel):

    def __init__(self, *args, database, fg_color = None, **kwargs):
        customtkinter.CTkToplevel.__init__(self, *args, fg_color=fg_color, **kwargs)

        self.__database = database
        self.geometry("400x280")
        self.label = customtkinter.CTkLabel(self, text="Ajouter un produit:", font=("Arial", 15, "bold"))
        self.label.grid(row=0, column=0, sticky="W", padx=10, pady=5)

        self.__name = customtkinter.CTkLabel(self, text="Nom:", font=("Arial", 12, "bold"))
        self.__name.grid(row=1, column=0, sticky="W", padx=10, pady=5)
        self.__description = customtkinter.CTkLabel(self, text="Description:", font=("Arial", 12, "bold"))
        self.__description.grid(row=2, column=0, sticky="W", padx=10, pady=5)
        self.__price = customtkinter.CTkLabel(self, text="Prix:", font=("Arial", 12, "bold"))
        self.__price.grid(row=3, column=0, sticky="W", padx=10, pady=5)
        self.__quantity = customtkinter.CTkLabel(self, text="Quantité:", font=("Arial", 12, "bold"))
        self.__quantity.grid(row=4, column=0, sticky="W", padx=10, pady=5)
        self.__category = customtkinter.CTkLabel(self, text="Catégorie:", font=("Arial", 12, "bold"))
        self.__category.grid(row=5, column=0, sticky="W", padx=10, pady=5)

        self.__name_entry = customtkinter.CTkEntry(self, width=200)
        self.__name_entry.grid(row=1, column=1, sticky="W", padx=10, pady=5)
        self.__description_entry = customtkinter.CTkEntry(self, width=200)
        self.__description_entry.grid(row=2, column=1, sticky="W", padx=10, pady=5)
        self.__price_entry = customtkinter.CTkEntry(self, width=50)
        self.__price_entry.grid(row=3, column=1, sticky="W", padx=10, pady=5)
        self.__quantity_entry = customtkinter.CTkEntry(self, width=50)
        self.__quantity_entry.grid(row=4, column=1, sticky="W", padx=10, pady=5)
        self.__category_entry = customtkinter.CTkEntry(self, width=50)
        self.__category_entry.grid(row=5, column=1, sticky="W", padx=10, pady=5)
        
        self.__add_button = customtkinter.CTkButton(self, text="Ajouter", width= 160, command=self.__add_product)
        self.__add_button.grid(row=6, column=0, sticky="W", padx=10, pady=5)
        self.__cancel_button = customtkinter.CTkButton(self, text="Annuler", width= 160, command=self.destroy)
        self.__cancel_button.grid(row=6, column=1, sticky="W", padx=10, pady=5)
        
        self.after(100,self.focus)


    def __add_product(self):
        new_product = Product(self.__database)
        new_product.create(self.__name_entry.get(),
                           self.__description_entry.get(),
                           self.__price_entry.get(),
                           self.__quantity_entry.get(),
                           self.__category_entry.get())
        self.destroy()
    
