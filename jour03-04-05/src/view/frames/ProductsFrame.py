import customtkinter
from src.view.windows.ModifyProductWindow import ModifyProductWindow
from src.model.Product import Product
from functools import partial

class ProductsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, products, title, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, master=master, label_text=title, **kwargs)

        # add widgets onto the frame...
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=2)
        self.columnconfigure(4, weight=2)
        self.columnconfigure(5, weight=1)
        
        self.__modify_product_window = None

        for i,product in enumerate(products):
            id = customtkinter.CTkButton(self, text=product.get_id(), command=partial(self.__product_action,product), width=20)
            id.grid(row=i, column=0, sticky="W", ipadx=10, ipady=5)
            name = customtkinter.CTkLabel(self, text=product.get_name(), font=("Arial", 12, "bold"))
            name.grid(row=i, column=1, sticky="W", ipadx=10, ipady=5)
            description = customtkinter.CTkLabel(self, text=product.get_description(), font=("Arial", 12, "bold"))
            description.grid(row=i, column=2, sticky="W", ipadx=10, ipady=5)
            price = customtkinter.CTkLabel(self, text=f"{product.get_price()}€", font=("Arial", 12, "bold"))
            price.grid(row=i, column=3, sticky="W", ipadx=10, ipady=5)
            quantity = customtkinter.CTkLabel(self, text=product.get_quantity(), font=("Arial", 12, "bold"))
            quantity.grid(row=i, column=4, sticky="W", ipadx=10, ipady=5)
            category = customtkinter.CTkLabel(self, text=product.get_id_category(), font=("Arial", 12, "bold"))
            category.grid(row=i, column=5, sticky="W", ipadx=10, ipady=5)
        

    def __product_action(self, product):

        if self.__modify_product_window is None or not self.__modify_product_window.winfo_exists():
            self.__modify_product_window = ModifyProductWindow(self, product=product)
            self.__modify_product_window.bind('<Destroy>',self.__call_self_destroy)
        else:
            self.__modify_product_window.focus()
        

    def __call_self_destroy(self,event):
        if event.widget == event.widget.winfo_toplevel():
            print("Destroying ProductFrame")
            self.destroy()