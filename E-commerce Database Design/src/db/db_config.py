from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

URL = "mysql+pymysql://root:root@localhost:3306/e_commercedb"
engine = create_engine(URL)
Session = sessionmaker(bind=engine,autoflush=False,autocommit=False)

class Base(DeclarativeBase):
    pass