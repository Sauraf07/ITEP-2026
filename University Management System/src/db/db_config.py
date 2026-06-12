from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy_serializer import SerializerMixin

DB_URL = "mysql+pymysql://root:root@localhost:3306/UMS"
engine = create_engine(DB_URL,echo=True)

session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase,SerializerMixin):
    pass
