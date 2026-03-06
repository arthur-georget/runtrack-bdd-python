import customtkinter

class ProductsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, master, label_text=title, **kwargs)

        self.__products = master.get_products()
        self.__categories = master.get_categories()

        # add widgets onto the frame...
        self.columnconfigure(0, weight=125)
        self.columnconfigure(1, weight=125)
        self.columnconfigure(2, weight=70)
        self.columnconfigure(3, weight=70)
        self.columnconfigure(4, weight=110)

        for i,product in enumerate(self.__products):
            name = customtkinter.CTkLabel(self, text=product.get_name(), font=("Arial", 12, "bold"))
            name.grid(row=i, column=0, sticky="W", ipadx=10, ipady=5)
            description = customtkinter.CTkLabel(self, text=product.get_description(), font=("Arial", 12, "bold"))
            description.grid(row=i, column=1, sticky="W", ipadx=10, ipady=5)
            price = customtkinter.CTkLabel(self, text=product.get_price(), font=("Arial", 12, "bold"))
            price.grid(row=i, column=2, sticky="W", ipadx=10, ipady=5)
            quantity = customtkinter.CTkLabel(self, text=product.get_quantity(), font=("Arial", 12, "bold"))
            quantity.grid(row=i, column=3, sticky="W", ipadx=10, ipady=5)
            category = customtkinter.CTkLabel(self, text=product.get_id_category(), font=("Arial", 12, "bold"))
            category.grid(row=i, column=4, sticky="W", ipadx=10, ipady=5)