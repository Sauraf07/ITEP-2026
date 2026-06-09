from sqlalchemy import create_engine, DateTime,func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped,mapped_column

DB_URL = "mysql+pymysql://root:root@localhost:3306/mysqlAlchemy"

engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(bind=engine,autoflush=False,autocommit=False)

class Base(DeclarativeBase):
    created_at:Mapped[DateTime] = mapped_column(DateTime,default=func.now())
    updated_at:Mapped[DateTime] = mapped_column(DateTime,default=func.now(),onupdate=func.now())