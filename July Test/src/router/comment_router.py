from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.repository_dependency import authenticate
from src.dependency.service_dependency import get_comments_service
from src.schema.comment import CommentRequest
from src.service.comment_service import CommentService

router = APIRouter(prefix="/comments", tags=["comments"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_comment(request: CommentRequest,user=Depends(authenticate),comment_service: CommentService = Depends(get_comments_service)):
    user_id = user.get("id")
    return await comment_service.create_comment(comment_text=request.comment, user_id=user_id, blog_id=request.blog_id)


@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
async def get_comments_by_blog(blog_id: int,payload=Depends(authenticate),comment_service: CommentService = Depends(get_comments_service)):
    return await comment_service.get_comments_by_blog(blog_id)


@router.delete("/{comment_id}", status_code=status.HTTP_200_OK)
async def delete_comment(comment_id: int,payload=Depends(authenticate),comment_service: CommentService = Depends(get_comments_service)):
    return await comment_service.delete_comment(comment_id)
