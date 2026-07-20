from src.models import User
from src.repository.user_repo import UserRepository
from src.schema.user import UserRequestBody, UserResponse
from src.utils.password import hash_password


class UserService:
    def __init__(self,user_repo:UserRepository):
        self.user_repo = user_repo


    async def register(self, request: UserRequestBody):
        user = User(name=request.name,email=request.email, password=hash_password(request.password))
        return await self.user_repo.register(user)

    async def login(self, request: UserResponse):
        return await self.user_repo.login(request.email, request.password)
    
    async def get_all_users(self):
        return await self.user_repo.get_all_users()