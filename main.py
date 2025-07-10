from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Smartphone", 600, 2)
p2 = Product("Laptop", 1000, 2)
p3 = Product("Headphones", 150, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.remove_product_by_name("Laptop")
print("After removal: ")
manager.display_products()
