from sqlalchemy import select
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
            
        