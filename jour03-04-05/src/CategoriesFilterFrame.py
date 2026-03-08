import customtkinter
from functools import partial

class CategoriesFilterFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, master, label_text=title, **kwargs)

        self.__categories = master.get_categories()
        self._scrollbar.configure(height=0)

        # add widgets onto the frame...
        
        for i,category in enumerate(self.__categories):
            name = customtkinter.CTkButton(self, text=category.get_name(), command=partial(self.__category_action,category.get_id()), width=20)
            name.grid(row=i, column=0, sticky="W", ipadx=10, ipady=5)

    def __category_action(self, id):
        pass
        print(id)