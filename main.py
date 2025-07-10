from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Phone", 500, 3)
p2 = Product("Laptop", 1000, 2)
p3 = Product("Headphones", 150, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()
print("Total inventory value:", manager.total_value())

manager.remove_product_by_name("Laptop")
print("After removal: ")
manager.display_products()

from cart import Cart

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p3)
cart.add_to_cart(p2)

cart.display_cart()
print("Ukupna vrednost za naplatu:", cart.total_cart_value())