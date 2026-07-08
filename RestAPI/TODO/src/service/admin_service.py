import email

from starlette.exceptions import HTTPException

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.models import Admin
from src.repository.admin_repo import AdminRepository
from src.schema.admin_schema import AdminRequest
from src.utils.password import hash_password
from src.utils.password import verify_password


class AdminService:
    def __init__(self,admin_repo:AdminRepository):
        self.admin_repo = admin_repo

    async def create(self,request:AdminRequest):
        admin = Admin(email=request.email,password=hash_password(request.password))
        return await self.admin_repo.create(admin)

    async def signin(self,request:AdminRequest):
        db_admin = await  self.admin_repo.fetch_by_email(request.email)
        if not db_admin:
            raise ResourceNotFoundException(f"User with email {request.email} not found")
        status = verify_password(request.password,db_admin.password)
        if not status:
            raise HTTPException(status_code=401,detail="Incorrect email or password")
        return db_admin