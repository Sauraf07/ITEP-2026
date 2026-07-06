import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./school.db")
engine = create_async_engine(URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def init_db() -> None:
    from src.model import ClassRoom, Student, Subject, Teacher  # noqa: F401

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
