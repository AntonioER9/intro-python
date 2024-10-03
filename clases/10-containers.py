class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def __str__(self):
        return f"{self.name} - {len(self.products)} products"

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)


kayal = Product("Kayal", 100)
laptop = Product("Laptop", 1500)
phone = Product("Phone", 800)
sports = Category("Sports")
sports.add_product(kayal)
