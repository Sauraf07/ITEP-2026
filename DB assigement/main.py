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



def
# delete_product_by_id()
# update_product_by_id()
# fetch_product_by_id()
# fetch_all_products()