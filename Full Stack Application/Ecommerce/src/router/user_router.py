from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.dependency.service_dependency import get_user_service
from src.schema.user_schema import TokenResponse, UserLoginRequest, UserRequest, UserResponse
from src.service import user_service
from src.service.user_service import UserService
from src.util.jwt_utils import generate_token

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/",
             status_code=status.HTTP_201_CREATED)

async def create_user(request:UserRequest,user_service = Depends(get_user_service)):
    return await user_service.create_user(request)


@router.post("/signin", status_code=status.HTTP_200_OK,response_model=TokenResponse)
async def login(request: UserLoginRequest, user_service: UserService = Depends(get_user_service)):
    db_user = await user_service.sign_in(request)
    return TokenResponse(email=db_user.email,name=db_user.name,token=generate_token({"id":db_user.id,"email":db_user.email}))



