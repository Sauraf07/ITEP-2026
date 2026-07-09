from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.user import User
from app.repository.user_repository import UserRepository
from app.schema.user_schema import UserLogin, UserRegister
from app.utils.jwt_handler import create_access_token
from app.utils.password import hash_password, verify_password


class AuthService:

    def __init__(self):
        self.repository = UserRepository()

    async def register(
        self,
        db: AsyncSession,
        user: UserRegister
    ):

        email = await self.repository.get_user_by_email(
            db,
            user.email
        )

        if email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )

        username = await self.repository.get_user_by_username(
            db,
            user.username
        )

        if username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )

        return await self.repository.create_user(
            db,
            new_user
        )

    async def login(
        self,
        db: AsyncSession,
        user: UserLogin
    ):

        db_user = await self.repository.get_user_by_email(
            db,
            user.email
        )

        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if not verify_password(
            user.password,
            db_user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect Password"
            )

        token = create_access_token(
            {
                "sub": str(db_user.id),
                "email": db_user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": db_user.id,
                "username": db_user.username,
                "email": db_user.email
            }
        }