class Product:
    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code


class Order:
    def __init__(self):
        self.product_list = []
        self.ordered_list = []

    def display_product_list(self):
        for product in self.product_list:
            print(f"{product.name} - {product.price} - {product.code}")

    def buy_product(self, product):
        self.ordered_list.append(product)

    def remove_product(self, product):
        self.ordered_list.remove(product)

    def display_order(self):
        print(f"Ordered products are {self.ordered_list}")
class Invoice:
    nextID = 0

    def __init__(self,name,invoice_number,products, total):




product1 = Product("laptop", 100, 123)
product2 = Product("cd", 200, 87)
