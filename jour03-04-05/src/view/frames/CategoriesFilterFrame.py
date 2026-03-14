import customtkinter
from functools import partial
from src.model.Category import Category

class CategoriesFilterFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, categories: list[Category], title, **kwargs):

        customtkinter.CTkScrollableFrame.__init__(self, master, label_text=title, **kwargs)

        self.__master = master

        self._scrollbar.configure(height=0)
        
        all_category_button = customtkinter.CTkButton(self, text='Tous', command= partial(self.__category_action,None), width=20)
        all_category_button.grid(row=0, column=0, sticky="W", pady=5)
        for i,category in enumerate(categories):
            # Sorry for the next line, it's pretty messy! I had no idea how to cleanly handle this event and pass it to the master widget
            category_button = customtkinter.CTkButton(self, text=category.get_name(), command= partial(self.__category_action,category.get_id()), width=20)
            category_button.grid(row=i+1, column=0, sticky="W", pady=5)

        self.__selected_id = None


    def __category_action(self, id: int | None):
        self.__selected_id = id
        self.__master.reinstantiate_frames(None)


    
    def get_selected_id(self):
        return self.__selected_id