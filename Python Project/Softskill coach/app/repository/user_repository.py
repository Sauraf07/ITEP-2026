from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.user import User


class UserRepository:

    async def create_user(
        self,
        db: AsyncSession,
        user: User
    ):
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def get_user_by_id(
        self,
        db: AsyncSession,
        user_id: int
    ):
        result = await db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_user_by_email(
        self,
        db: AsyncSession,
        email: str
    ):
        result = await db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_user_by_username(
        self,
        db: AsyncSession,
        username: str
    ):
        result = await db.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()

    async def get_all_users(
        self,
        db: AsyncSession
    ):
        result = await db.execute(select(User))
        return result.scalars().all()

    async def delete_user(
        self,
        db: AsyncSession,
        user: User
    ):
        await db.delete(user)
        await db.commit()