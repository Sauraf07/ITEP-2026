from fastapi import APIRouter, Depends, File, Form, UploadFile
from starlette import status

from src.dependency.repository_dependency import authenticate
from src.dependency.service_dependency import get_blog_service
from src.service.blog_service import BlogService

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog(
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(...),
    user_id: int = Form(...),
    category_id: int = Form(...),
    blog_service: BlogService = Depends(get_blog_service),blog=Depends(authenticate)
):
    return await blog_service.create_blog(title=title,content=content, blog_image=image,user_id=user_id,category_id=category_id,)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_blogs(blog_service: BlogService = Depends(get_blog_service),blog=Depends(authenticate)):
    return await blog_service.get_all_blogs()

@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
async def get_blog_by_id(blog_id: int, blog_service: BlogService = Depends(get_blog_service),blog=Depends(authenticate)):
    return await blog_service.get_blog_by_id(blog_id)

@router.delete("/{blog_id}", status_code=status.HTTP_200_OK)
async def delete_blog(blog_id: int, blog_service: BlogService = Depends(get_blog_service),blog=Depends(authenticate)):
    return await blog_service.delete_blog(blog_id)

@router.put("/{blog_id}", status_code=status.HTTP_200_OK)
async def update_blog(blog_id: int, title: str = Form(...), content: str = Form(...), blog_service: BlogService = Depends(get_blog_service),blog=Depends(authenticate)):
    updated_blog = {"title": title, "content": content}
    return await blog_service.update_blog(blog_id, updated_blog)
