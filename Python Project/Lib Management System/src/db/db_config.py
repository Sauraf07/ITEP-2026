from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

URL = "mysql+asyncmy://root:root@localhost:3306/lib"
engine = create_async_engine(URL)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
print("Database connected...")
class Base(DeclarativeBase):
    pass