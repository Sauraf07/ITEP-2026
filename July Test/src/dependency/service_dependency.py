from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_config import get_session
from src.dependency.repository_dependency import get_user_repo, get_categories_repo
from src.repository.catagories_repo import CategoriesRepository
from src.repository.user_repo import UserRepository
from src.service.catagories_service import CategoriesService
from src.service.user_service import UserService

from src.repository.bolg_repo import BlogRepo
from src.service.blog_service import BlogService


def get_user_service(session: AsyncSession = Depends(get_session),user_repo: UserRepository = Depends(get_user_repo),):
    return UserService(user_repo)


def get_catagories_service(session: AsyncSession = Depends(get_session),cata_repo: CategoriesRepository = Depends(get_categories_repo),):
    return CategoriesService(cata_repo)


def get_blog_service(session: AsyncSession = Depends(get_session),):
    return BlogService(BlogRepo(session))
