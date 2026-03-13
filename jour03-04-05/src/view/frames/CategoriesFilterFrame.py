import customtkinter
from functools import partial
from src.model.Category import Category

class CategoriesFilterFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, categories: list[Category], title, **kwargs):

        customtkinter.CTkScrollableFrame.__init__(self, master, label_text=title, **kwargs)

        self._scrollbar.configure(height=0)
        
        for i,category in enumerate(categories):
            name = customtkinter.CTkButton(self, text=category.get_name(), command=partial(self.__category_action,category.get_id()), width=20)
            name.grid(row=i, column=0, sticky="W", pady=5)

        self.__selected_id = None


    def __category_action(self, id):
        self.__selected_id = id

    
    def get_selected_id(self):
        return self.__selected_id