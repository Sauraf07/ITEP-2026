import bcrypt
from alembic.util import status
from fastapi import HTTPException

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.models import User
from src.repository.user_repository import UserRepository
from src.schema.user_schema import UserRequest
from src.util.jwt_utils import generate_token,verify_token
from src.util.password_util import hash_password, verify_password


class UserService:
    def __init__(self,user_repo:UserRepository):
        self.user_repo = user_repo

    async def create_user(self,request:UserRequest):
        user = User(
            name=request.name,
            email=request.email,
            password=hash_password(request.password),
            contact=request.contact
        )
        return await self.user_repo.create(user)

    async def fetch_all(self):
        return self.user_repo.fetch_all()

    async def sign_in(self,request:UserRequest):
        db_user =  await self.user_repo.fetch_by_email(request.email)
        if not db_user:
            raise ResourceNotFoundException(f'{request.email} is not registered')
        status = verify_password(request.password,db_user.password)
        if not status:
            raise HTTPException(status_code=401,detail="Incorrect Password")
        return db_user