from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
DB_URl = 'mysql+pymysql://root:root@localhost:3306/dbtest1'
engine = create_engine(DB_URl,) #echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("Database connected")
class Base(DeclarativeBase):
    pass