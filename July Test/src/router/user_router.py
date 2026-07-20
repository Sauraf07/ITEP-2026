from fastapi import APIRouter, Depends
from starlette import status
from src.dependency.service_dependency import get_user_service
from src.schema.user import UserRequestBody, UserResponse, Token
from src.service.user_service import UserService
from src.utils.jwt_utils import generate_token

router = APIRouter(prefix="/user",tags=["user"])

@router.post("/",status_code=status.HTTP_201_CREATED)
async def register(request: UserRequestBody,user_service:UserService=Depends(get_user_service)):
    user = await user_service.register(request)
    return user

@router.post("/login",status_code=status.HTTP_200_OK,response_model=Token)
async def login(request: UserResponse,user_service:UserService=Depends(get_user_service)):
    db_user = await user_service.login(request)
    return Token(email=db_user.email,token=generate_token(({"id":db_user.id,"email":db_user.email})))

@router.get("/profile",status_code=status.HTTP_200_OK)
async def profile(user_service:UserService=Depends(get_user_service)):
    return await user_service.get_all_users()