from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase

URL = "mysql+asyncmy://root:root@localhost:3306/school"
engine = create_async_engine(URL,echo=True)

SessionLocal = async_sessionmaker(bind=engine,expire_on_commit=False)
print("Database Connected....")
class Base(DeclarativeBase):
    pass


