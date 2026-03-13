import customtkinter
from src.model.Category import Category

class AddCategoryInputDialog(customtkinter.CTkToplevel):

    def __init__(self, *args, database, fg_color = None, **kwargs):
        customtkinter.CTkToplevel.__init__(self, *args, fg_color=fg_color, **kwargs)

        self.__database = database
        self.geometry("400x280")
        self.label = customtkinter.CTkLabel(self, text="Ajouter un categorie:", font=("Arial", 15, "bold"))
        self.label.grid(row=0, column=0, sticky="W", padx=10, pady=5)

        self.__name = customtkinter.CTkLabel(self, text="Nom:", font=("Arial", 12, "bold"))
        self.__name.grid(row=1, column=0, sticky="W", padx=10, pady=5)

        self.__name_entry = customtkinter.CTkEntry(self, width=200)
        self.__name_entry.grid(row=1, column=1, sticky="W", padx=10, pady=5)
        
        self.__add_button = customtkinter.CTkButton(self, text="Ajouter", width= 160, command=self.__add_category)
        self.__add_button.grid(row=6, column=0, sticky="W", padx=10, pady=5)
        self.__cancel_button = customtkinter.CTkButton(self, text="Annuler", width= 160, command=self.destroy)
        self.__cancel_button.grid(row=6, column=1, sticky="W", padx=10, pady=5)
        
        self.after(100,self.focus)


    def __add_category(self):
        new_category = Category(self.__database)
        new_category.create(self.__name_entry.get())
        self.destroy()