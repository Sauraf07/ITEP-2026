from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.exceptions import HTTPException

from src.db.db_config import get_session
from src.repository.cart_items_repository import CartItemsRepository
from src.repository.cart_repository import CartRepository
from src.repository.category_repository import CategoryRepository
from src.repository.order_repository import OrderRepository
from src.repository.product_repository import ProductRepository
from src.repository.user_repository import UserRepository
from src.util.jwt_utils import verify_token

security = HTTPBearer()

def authenticate(header: HTTPAuthorizationCredentials = Depends(security)):
    token = header.credentials
    if not token:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    payload = verify_token(token)
    return payload
def get_user_repository(session:AsyncSession=Depends(get_session)):
    return UserRepository(session)

def get_category_repository(session:AsyncSession=Depends(get_session)):
    return CategoryRepository(session)

def get_product_repository(session:AsyncSession=Depends(get_session)):
    return ProductRepository(session)
def get_cart_repository(session:AsyncSession=Depends(get_session)):
    return CartRepository(session)

def get_cart_items_repository(session:AsyncSession=Depends(get_session)):
    return CartItemsRepository(session)

def get_order_repository(session:AsyncSession=Depends(get_session)):
    return OrderRepository(session)