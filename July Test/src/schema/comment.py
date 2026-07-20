from pydantic import BaseModel


class CommentRequest(BaseModel):
    comment:str
    user_id:int
    blog_id:int