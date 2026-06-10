from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy_serializer import SerializerMixin

DB_URL = "mysql+pymysql://root:root@localhost:3306/testrelationship"
engine = create_engine(DB_URL,echo=True)

Sessionlocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

class Base(DeclarativeBase,SerializerMixin):
    pass