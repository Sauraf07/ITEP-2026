from fastapi import Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.db_config import get_session
from src.utils.jwt_util import verify_token
from starlette.exceptions import HTTPException
from src.repository.admin_repository import AdminRepository
from src.services.admin_service import AdminService
security = HTTPBearer()

def authenticate(header: HTTPAuthorizationCredentials = Depends(security)):
    token = header.credentials
    if not token:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    payload = verify_token(token)
    return payload

def get_admin_respository(session:AsyncSession=Depends(get_session)):
    return AdminRepository(session)

def get_admin_service(admin_repo:AdminRepository=Depends(get_admin_respository)):
    return AdminService(admin_repo)