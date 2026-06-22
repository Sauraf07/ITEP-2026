from src.dao.user_dao import UserDao


class UserService:
    def __init__(self,session):
        self.user_dao = UserDao(session)

    async def create_user(self,user):
        return await self.user_dao.create_user(user)
    
    async def get_all_users(self):
        return await self.user_dao.get_all_users()
    
    async def get_user_by_id(self,user_id:int):
        return await self.user_dao.get_user_by_id(user_id)
    
    async def update_user(self,user):
        return await self.user_dao.update_user(user)
    
    async def delete_user(self,user):
        return await self.user_dao.delete_user(user)