from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.model import Product
from src.service import product_service
from src.service.product_service import ProductService


def create_product():
    try:
        with SessionLocal.begin() as session:
            title = input("Enter product title: ")
            price = float(input("Enter product price: "))
            brand = input("Enter product brand: ")
            category = input("Enter product category: ")
            dp = float(input("Enter product discount Percentage: "))
            p = Product(title=title,price=price,brand=brand,category_name=category,discount_percentage=dp)
            product_service = ProductService(session)
            
    except SQLAlchemyError as e:
        print(e)