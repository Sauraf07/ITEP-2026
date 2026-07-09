from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schema.user_schema import UserResponse
from app.service.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserService()


@router.get(
    "/",
    response_model=list[UserResponse]
)
async def get_all_users(
    db: AsyncSession = Depends(get_db)
):
    return await service.get_all_users(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await service.get_user_by_id(
        db,
        user_id
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    await service.delete_user(
        db,
        user_id
    )