from sqlalchemy.orm import session

from src.dao.product_dao import ProductDao
from src.model.product import Product

def add_product():
    title = input("Enter product title: ")
    price = float(input("Enter product price: "))
    discount_percent = float(input("Enter product discount percent: "))
    brand= input("Enter product brand: ")
    category_name = input("Enter product category name: ")
    product = Product(title=title, price=price, discount_percent=discount_percent,brand=brand,catagory_name=category_name)
    if ProductDao.save_product(product):
        print("Product added successfully.")
    else:
        print("Failed to add product.")

def fetch_all_products():
    products = ProductDao.get_all_products()



def fetch_product_by_id():
    id = input("Enter product id: ")
    product = ProductDao.get_product_by_id(id)

def update_product_by_id():
    id = input("Enter product id to update: ")
    title = input("Enter new product title: ")
    price = float(input("Enter new product price: "))
    discount_percent = float(input("Enter new product discount percent: "))
    brand= input("Enter new product brand: ")
    category_name = input("Enter new product category name: ")
    updated_product = Product(title=title, price=price, discount_percent=discount_percent,brand=brand,catagory_name=category_name)
    if ProductDao.update_product(updated_product, id):
        print("Product updated successfully.")
    else:
        print("Failed to update product.")
   


def delete_product_by_id():
    id = input("Enter product id to delete: ")
    if ProductDao.delete_product(id):
        print("Product deleted successfully.")
    else:
        print("Failed to delete product.")



def fetch_by_brand():
    brand = input("Enter product brand to fetch: ")
    products = ProductDao.find_by_brand(brand)
    if products:
        for product in products:
            print(f"{product.id} : {product.title}")
    else:
        print("No products found for the given brand.")


def find_by_category():
    category = input("Enter product category to fetch: ")
    products = ProductDao.find_by_category(category)
    if products:
        for product in products:
            print(f"{product.id} : {product.title}")
    else:
        print("No products found for the given category.")



def fetch_product_grater_than_price():
    price = float(input("Enter price to fetch products greater than: "))
    products = ProductDao.fetch_product_greater_than_price(price)
    if products:
        for product in products:
            print(f"{product.id} : {product.title}")
        else:
            print("No products found greater than the given price.")

def get_products_by_percent_discount():
    discount_percent = float(input("Enter discount percent to fetch products greater than: "))
    products = ProductDao.get_products_by_percent_discount(discount_percent)
    if products:
        for product in products:
            print(f"{product.id} : {product.title}")
        else:
            print("No products found with discount percent greater than the given value.")
    
def and_condition_example():
    price = float(input("Enter price to fetch products greater than: "))
    discount_percent = float(input("Enter discount percent to fetch products greater than: "))
    products = ProductDao.and_condition_example(price, discount_percent)
    if products:
        for product in products:
            print(f"{product.id} : {product.title}")
        else:
            print("No products found matching the given conditions.")
def or_condition_example():
    price = float(input("Enter price to fetch products greater than: "))
    discount_percent = float(input("Enter discount percent to fetch products greater than: "))
    products = ProductDao.or_condition_example(price, discount_percent)
    if products:
        for product in products:
            print(f"{product.id} : {product.title}")
        else:
            print("No products found matching the given conditions.")

def order_by_price_asc():
    products = ProductDao.order_by_price_asc()
    if products:
        for product in products:
            print(f"{product.id} : {product.title} - {product.price}")
        else:
            print("No products found.")

def order_by_price_desc():
    products = ProductDao.order_by_price_desc()
    if products:
        for product in products:
            print(f"{product.id} : {product.title} - {product.price}")
        else:
            print("No products found.")

def count_products_by_brand():
    print("Counting products by brand...")
    ProductDao.count_products_by_brand()
    
def avg_price_by_category():
    ProductDao.avg_price_by_category()

def find_all_laptops():
    products = ProductDao.find_all_laptops()
    if products:
        for product in products:
            print(f"{product.id} : {product.title} - {product.price}")
        else:
            print("No laptop products found.")
def most_expensive_product():
    product = ProductDao.most_expensive_product()
    if product:
        print(f"Most expensive product: {product.id} : {product.title} - {product.price}")
    else:
        print("No products found.")
most_expensive_product()
# find_all_laptops()
# avg_price_by_category()
# count_products_by_brand()
# order_by_price_desc()
# order_by_price_asc()
# or_condition_example()
# and_condition_example()
# get_products_by_percent_discount()
# fetch_product_grater_than_price()
# find_by_category()
# fetch_by_brand()
# delete_product_by_id()
# update_product_by_id()
# fetch_product_by_id()
# fetch_all_products()