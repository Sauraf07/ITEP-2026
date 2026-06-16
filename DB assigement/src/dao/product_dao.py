from sqlalchemy import func, select
from sqlalchemy.exc import SQLAlchemyError

from src.model.product import Product
from src.db.db_config import SessionLocal

class ProductDao:
    @staticmethod
    def save_product(p: Product):
        session = None
        try:
            with SessionLocal() as session:
                session.add(p)
                session.commit()
                return True
        except SQLAlchemyError as e:
            if session is not None:
                session.rollback()
            print(e)

    @staticmethod
    def get_all_products():
          try:
            with SessionLocal() as session:
                statement = select(Product)
                products = session.execute(statement).scalars().all()
                #print(products)
                for product in products:
                    print(f"{product.id} : {product.title}")
          except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def get_product_by_id(id: int):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.id == id)
                result = session.execute(statement).scalars().fetchmany()
                for product in result:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def update_product(p:Product,product_id:int):
        session = None
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.id == product_id)
                result = session.execute(statement).first()
                if result is not None:
                    product_to_update = result[0]
                    product_to_update.title = p.title
                    product_to_update.price = p.price
                    product_to_update.discount_percent = p.discount_percent
                    product_to_update.brand = p.brand
                    product_to_update.catagory_name = p.catagory_name
                    session.commit()
                    return True
                else:
                    print(f"Product with id {product_id} not found.")
                    return False
        except SQLAlchemyError as e:
            if session is not None:
                session.rollback()
            print(e)

    @staticmethod
    def delete_product(product_id: int):
        session = None
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.id == product_id)
                result = session.execute(statement).first()
                if result is not None:
                    product_to_delete = result[0]
                    session.delete(product_to_delete)
                    session.commit()
                    return True
                else:
                    print(f"Product with id {product_id} not found.")
                    return False
        except SQLAlchemyError as e:
            if session is not None:
                session.rollback()
            print(e)

    @staticmethod
    def find_by_brand(brand_name):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.brand == brand_name)
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)
            
    @staticmethod
    def find_by_category(category):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.catagory_name == category)
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def fetch_product_greater_than_price(price):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.price > 70000)
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def get_products_by_percent_discount(discount_percent):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.discount_percent > discount_percent)
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def and_condition_example(price, discount_percent):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.price > price and Product.discount_percent > discount_percent)
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def or_condition_example(price, discount_percent):
        try:
            with SessionLocal() as session:
                statement = select(Product).where((Product.price > price) or (Product.discount_percent > discount_percent))
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def order_by_price_asc():
        try:
            with SessionLocal() as session:
                statement = select(Product).order_by(Product.price.asc())
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title} - {product.price}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def order_by_price_desc():
        try:
            with SessionLocal() as session:
                statement = select(Product).order_by(Product.price.desc())
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title} - {product.price}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def count_products_by_brand():
        try:
            with SessionLocal() as session:
                statement = select(Product.brand, func.count(Product.id)).group_by(Product.brand)
                results = session.execute(statement).all()
                for brand, count in results:
                    print(f"Brand: {brand}, Count: {count}")
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def avg_price_by_category():
        try:
            with SessionLocal() as session:
                statement = select(Product.catagory_name, func.avg(Product.price)).group_by(Product.catagory_name)
                results = session.execute(statement).all()
                for category, avg_price in results:
                    print(f"Category: {category}, Average Price: {avg_price}")
        except SQLAlchemyError as e:
            print(e)
        
    @staticmethod
    def find_all_laptops():
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.catagory_name == 'Laptop')
                products = session.execute(statement).scalars().all()
                for product in products:
                    print(f"{product.id} : {product.title}")
        except SQLAlchemyError as e:
            print(e)
    
    @staticmethod
    def most_expensive_product():
        try:
            with SessionLocal() as session:
                statement = select(Product).order_by(Product.price.desc()).limit(1)
                product = session.execute(statement).scalar_one_or_none()
                if product:
                    print(f"Most Expensive Product: {product.id} : {product.title} - {product.price}")
                else:
                    print("No products found.")
        except SQLAlchemyError as e:
            print(e)
        