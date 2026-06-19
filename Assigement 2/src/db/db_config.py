from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_URl = "mysql+pymysql://root:root@localhost:3306/library"
engine = create_engine(DB_URl)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("Data Base Connected")
class Base(DeclarativeBase):
    pass
