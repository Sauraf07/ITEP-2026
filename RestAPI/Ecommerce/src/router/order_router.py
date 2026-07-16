from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.repository_dependency import authenticate

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/placeorder",status_code=status.HTTP_201_CREATED)
async def place_order(payload:dict=Depends(authenticate)):
    pass