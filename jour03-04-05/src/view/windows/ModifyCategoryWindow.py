import customtkinter
from src.model.Category import Category
from src.view.windows.ConfirmDeleteElementWindow import ConfirmDeleteElementWindow

class ModifyCategoryWindow(customtkinter.CTkToplevel):

    def __init__(self, *args, category: Category ,fg_color = None, **kwargs):
        customtkinter.CTkToplevel.__init__(self, *args, fg_color=fg_color, **kwargs)
        self.__category = category

        self.geometry("550x250")
        self.label = customtkinter.CTkLabel(self, text="Gestion de la catégorie", font=("Arial", 15, "bold"))
        self.label.grid(row=0, column=0, sticky="W", padx=10, pady=5)

        self.__modify_name_button = customtkinter.CTkButton(self, text="Modifier le nom", width= 160, command=self.__modify_category_name_dialog)
        self.__modify_name_button.grid(row=1, column=1, sticky="W", padx=10, pady=5)

        self.__delete_category_button = customtkinter.CTkButton(self, text="Supprimer le catégorie", width= 160, fg_color="red3", hover_color="red4", command=self.__delete_category_dialog)
        self.__delete_category_button.grid(row=5, column=0, sticky="W", padx=10, pady=5)

        self.__name = customtkinter.CTkLabel(self, text=self.__category.get_name(), font=("Arial", 12, "bold"))
        self.__name.grid(row=1, column=2, sticky="W", padx=10, pady=5)

        self.__delete_confirm_dialog = None

        self.after(100,self.focus)


    def __modify_category_name_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Nouveau nom:", title="Changer le nom de la catégorie")
        user_input = dialog.get_input()
        if user_input is not None:
            self.__category.update_name(user_input)
            self.destroy()


    def __delete_category_dialog(self):
        if self.__delete_confirm_dialog is None or not self.__delete_confirm_dialog.winfo_exists():
            self.__delete_confirm_dialog = ConfirmDeleteElementWindow(self, category=self.__category)
            self.__delete_confirm_dialog.bind('<Destroy>',self.__call_self_destroy)
        else:
            self.__delete_confirm_dialog.focus()


    def __call_self_destroy(self, event):
        if event.widget == event.widget.winfo_toplevel():
            print("Destroying ModifyCategoryWindow")
            self.destroy()