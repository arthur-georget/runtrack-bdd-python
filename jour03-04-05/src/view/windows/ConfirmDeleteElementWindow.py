import customtkinter
from src.model.Category import Category
from src.model.Product import Product

class ConfirmDeleteElementWindow(customtkinter.CTkToplevel):

    def __init__(self, master, element: Category | Product, fg_color = None, **kwargs):
        customtkinter.CTkToplevel.__init__(self, master=master, fg_color=fg_color, **kwargs)
        self.__element = element
        self.geometry("550x100")
        self.label = customtkinter.CTkLabel(self, text=f"Voulez vous vraiment supprimer '{element.get_name()}'?", font=("Arial", 15, "bold"))
        self.label.grid(row=0, column=0, columnspan=3 ,sticky="W", padx=10, pady=5)

        self.__yes_button = customtkinter.CTkButton(self, text="Oui", width= 160, command=self.__delete_element)
        self.__yes_button.grid(row=1, column=0, sticky="W", padx=10, pady=5)
        self.__no_button = customtkinter.CTkButton(self, text="Non", width= 160, command=self.destroy)
        self.__no_button.grid(row=1, column=1, sticky="W", padx=10, pady=5)
        self.__cancel_button = customtkinter.CTkButton(self, text="Annuler", width= 160, command=self.destroy)
        self.__cancel_button.grid(row=1, column=2, sticky="W", padx=10, pady=5)

        self.after(100,self.focus)


    def __delete_element(self):

        self.__element.delete()
        print("Destroying ConfirmDeleteElementWindow")
        self.destroy()