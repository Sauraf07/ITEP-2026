from src.models import User
from src.repository.user_repository import UserRepository
from src.schema.user_schema import UserRequest
from src.util.password_util import hash_password


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