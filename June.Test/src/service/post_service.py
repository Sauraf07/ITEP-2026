from src.dao.post_dao import PostDao


class PostService:
    def __init__(self,session):
        self.post_dao = PostDao(session)

    async def create_post(self,post):
        return await self.post_dao.create_post(post)
    
    async def get_all_posts(self):
        return await self.post_dao.get_all_posts()
    
    async def fetch_post_by_id(self,post_id:int):
        return await self.post_dao.fetch_post_by_id(post_id)
    
    async def update_post(self,post):
        return await self.post_dao.update_post(post)
    
    async def delete_post(self,post):
        return await self.post_dao.delete_post(post)