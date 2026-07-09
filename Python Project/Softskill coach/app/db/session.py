from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_config import SessionLocal

async def get_db():
    async with SessionLocal() as session:
        yield session
