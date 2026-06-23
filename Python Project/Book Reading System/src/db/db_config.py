from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Session, DeclarativeBase

URl = "mysql+asyncmy://root:root@localhost:3306/book"

engine = create_async_engine(URl)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
print("Database connected")
class Base(DeclarativeBase):
    pass