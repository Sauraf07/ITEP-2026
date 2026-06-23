from sqlalchemy import select

from src.model.user import User


class UserDao:
    def __init__(self,session):
        self.session = session

    async def create_user(self,user:User):
        self.session.add(user)
        await self.session.commit()
        return user
    
    async def get_all_users(self):
        statement = select(User)
        results = await self.session.execute(statement)
        users = results.scalars().all()
        return users

    async def get_user_by_id(self,user_id:int):
        statement = select(User).where(User.id == user_id)
        result = await self.session.execute(statement)
        user = result.scalars().all()
        return user
    
    async def update_user(self,user:User):
        await self.session.commit()
        return user
    
    async def delete_user(self,user:User):
        await self.session.delete(user)
        await self.session.commit()
        return None