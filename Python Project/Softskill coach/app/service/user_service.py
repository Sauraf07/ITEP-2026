from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    async def get_all_users(
        self,
        db: AsyncSession
    ):
        return await self.repository.get_all_users(db)

    async def get_user_by_id(
        self,
        db: AsyncSession,
        user_id: int
    ):

        user = await self.repository.get_user_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    async def delete_user(
        self,
        db: AsyncSession,
        user_id: int
    ):

        user = await self.get_user_by_id(
            db,
            user_id
        )

        await self.repository.delete_user(
            db,
            user
        )