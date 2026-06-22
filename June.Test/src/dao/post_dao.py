from sqlalchemy import select

from src.model.post  import Post


class PostDao:
    def __init__(self,session):
        self.session = session

    async def create_post(self,post:Post):
        self.session.add(post)
        await self.session.commit()
        return post
       
    
    async def get_all_posts(self):
        statement = select(Post)
        results = await self.session.execute(statement)
        posts = results.scalars().all()
        return posts

    async def fetch_post_by_id(self,post_id:int):
        statement = select(Post).where(Post.id == post_id)
        result = await self.session.execute(statement)
        post = result.scalars().all()
        return post
    
    async def update_post(self,post:Post):
        await self.session.commit()
        return post
    
    async def delete_post(self,post:Post):
        await self.session.delete(post)
        await self.session.commit()
        return post