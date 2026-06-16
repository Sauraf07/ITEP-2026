from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

URL_DB = 'mysql+pymysql://root:root@localhost:3306/assigement'
engine = create_engine(URL_DB, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("DataBase connected")

class Base(DeclarativeBase):
    pass