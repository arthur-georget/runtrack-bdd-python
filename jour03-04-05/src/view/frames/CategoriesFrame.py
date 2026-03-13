import customtkinter
from functools import partial
from src.model.Category import Category
from src.view.windows.ModifyCategoryWindow import ModifyCategoryWindow


class CategoriesFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, categories: list[Category], title, **kwargs):
        
        customtkinter.CTkScrollableFrame.__init__(self, master=master, label_text=title, **kwargs)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        
        self.__modify_category_window = None

        for i,category in enumerate(categories):
            id = customtkinter.CTkButton(self, text=category.get_id(), command=partial(self.__category_action,category), width=20)
            id.grid(row=i, column=0, sticky="W", ipadx=10, ipady=5)
            name = customtkinter.CTkLabel(self, text=category.get_name(), font=("Arial", 12, "bold"))
            name.grid(row=i, column=1, sticky="W", ipadx=10, ipady=5)
        

    def __category_action(self, category: Category):

        if self.__modify_category_window is None or not self.__modify_category_window.winfo_exists():
            self.__modify_category_window = ModifyCategoryWindow(self, category=category)
            self.__modify_category_window.bind('<Destroy>',self.__call_self_destroy)

        else:
            self.__modify_category_window.focus()
        

    def __call_self_destroy(self,event):

        if event.widget == event.widget.winfo_toplevel():
            print("Destroying CategoryFrame")
            self.destroy()