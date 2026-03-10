import customtkinter
from src.model.Product import Product
from src.view.windows.ConfirmDeleteProductWindow import ConfirmDeleteProductWindow

class ModifyProductWindow(customtkinter.CTkToplevel):

    def __init__(self, *args, product: Product ,fg_color = None, **kwargs):
        customtkinter.CTkToplevel.__init__(self, *args, fg_color=fg_color, **kwargs)
        self.__product = product

        self.geometry("550x250")
        self.label = customtkinter.CTkLabel(self, text="Gestion du produit", font=("Arial", 15, "bold"))
        self.label.grid(row=0, column=0, sticky="W", padx=10, pady=5)

        self.__modify_name_button = customtkinter.CTkButton(self, text="Modifier le nom", width= 160, command=self.__modify_product_name_dialog)
        self.__modify_name_button.grid(row=1, column=1, sticky="W", padx=10, pady=5)
        self.__modify_description_button = customtkinter.CTkButton(self, text="Modifier la description", width= 160, command=self.__modify_product_description_dialog)
        self.__modify_description_button.grid(row=2, column=1, sticky="W", padx=10, pady=5)
        self.__modify_price_button = customtkinter.CTkButton(self, text="Modifier le prix", width= 160, command=self.__modify_product_price_dialog)
        self.__modify_price_button.grid(row=3, column=1, sticky="W", padx=10, pady=5)
        self.__modify_quantity_button = customtkinter.CTkButton(self, text="Modifier la quantité", width= 160, command=self.__modify_product_quantity_dialog)
        self.__modify_quantity_button.grid(row=4, column=1, sticky="W", padx=10, pady=5)
        self.__modify_category_button = customtkinter.CTkButton(self, text="Modifier la catégorie", width= 160, command=self.__modify_product_category_dialog)
        self.__modify_category_button.grid(row=5, column=1, sticky="W", padx=10, pady=5)
        self.__delete_product_button = customtkinter.CTkButton(self, text="Supprimer le produit", width= 160, fg_color="red3", hover_color="red4", command=self.__delete_product_dialog)
        self.__delete_product_button.grid(row=5, column=0, sticky="W", padx=10, pady=5)

        self.__name = customtkinter.CTkLabel(self, text=self.__product.get_name(), font=("Arial", 12, "bold"))
        self.__name.grid(row=1, column=2, sticky="W", padx=10, pady=5)
        self.__description = customtkinter.CTkLabel(self, text=self.__product.get_description(), font=("Arial", 12, "bold"))
        self.__description.grid(row=2, column=2, sticky="W", padx=10, pady=5)
        self.__price = customtkinter.CTkLabel(self, text=f"{self.__product.get_price()}€", font=("Arial", 12, "bold"))
        self.__price.grid(row=3, column=2, sticky="W", padx=10, pady=5)
        self.__quantity = customtkinter.CTkLabel(self, text=self.__product.get_quantity(), font=("Arial", 12, "bold"))
        self.__quantity.grid(row=4, column=2, sticky="W", padx=10, pady=5)
        self.__category = customtkinter.CTkLabel(self, text=self.__product.get_id_category(), font=("Arial", 12, "bold"))
        self.__category.grid(row=5, column=2, sticky="W", padx=10, pady=5)

        self.__delete_confirm_dialog = None

        self.after(100,self.focus)


    def __modify_product_name_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Nouveau nom:", title="Changer le nom du produit")
        user_input = dialog.get_input()
        if user_input is not None:
            self.__product.update_name(user_input)
            self.master.destroy()

    def __modify_product_description_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Nouvelle description:", title="Changer la description du produit")
        user_input = dialog.get_input()
        if user_input is not None:
            self.__product.update_description(user_input)
            self.master.destroy()

    def __modify_product_price_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Nouveau prix:", title="Changer le prix du produit")
        user_input = dialog.get_input()
        if user_input is not None:
            self.__product.update_price(user_input)
            self.master.destroy()

    def __modify_product_quantity_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Nouvelle quantité:", title="Changer la quantité de produit")
        user_input = dialog.get_input()
        if user_input is not None:
            self.__product.update_quantity(user_input)
            self.master.destroy()


    def __modify_product_category_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Nouvelle catégorie:", title="Changer la catégorie du produit")
        user_input = dialog.get_input()
        if user_input is not None:
            self.__product.update_category(user_input)
            self.master.destroy()

    def __delete_product_dialog(self):
        if self.__delete_confirm_dialog is None or not self.__delete_confirm_dialog.winfo_exists():
            self.__delete_confirm_dialog = ConfirmDeleteProductWindow(self, product=self.__product)
        else:
            self.__delete_confirm_dialog.focus()