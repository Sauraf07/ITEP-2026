
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.exceptions import HTTPException

from src.db.db_config import get_session
from src.repository.bolg_repo import BlogRepo
from src.repository.catagories_repo import CategoriesRepository
from src.repository.comment_repo import CommentRepository
from src.repository.user_repo import UserRepository
from src.utils.jwt_utils import verify_token

security = HTTPBearer()

def authenticate(headers:HTTPAuthorizationCredentials=Depends(security)):
    token = headers.credentials
    if not token:
        raise HTTPException(status_code=401,detail="Authentication credentials were not provided")
    payload = verify_token(token)
    return payload

def get_user_repo(session:AsyncSession=Depends(get_session)):
    return UserRepository(session)

def get_categories_repo(session:AsyncSession=Depends(get_session)):
    return CategoriesRepository(session)

def get_blog_repo(session:AsyncSession=Depends(get_session)):
    return BlogRepo(session)

def get_comments_repo(session:AsyncSession=Depends(get_session)):
    return CommentRepository(session)