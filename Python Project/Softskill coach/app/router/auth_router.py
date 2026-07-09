from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schema.user_schema import (
    UserLogin,
    UserRegister,
    UserResponse
)
from app.service.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

service = AuthService()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
async def register(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    return await service.register(
        db,
        user
    )


@router.post("/login")
async def login(
    user: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    return await service.login(
        db,
        user
    )