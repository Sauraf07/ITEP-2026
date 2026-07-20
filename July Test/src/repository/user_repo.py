from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.password import verify_password
from src.excaption.resource_not_found_handler import ResourceNotFound
from src.models import User
from src.schema.user import UserRequestBody


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register(self, user: UserRequestBody):
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def get_user_by_email(self, email: str):
        user = await self.session.execute(select(User).where(User.email == email))
        return user.scalar_one_or_none()

    async def login(self, email: str, password: str):
        db_user = await self.get_user_by_email(email)
        if not db_user:
            raise ResourceNotFound("email not found")

        email_match = db_user.email == email
        password_match = verify_password(password, db_user.password)

        if not email_match or not password_match:
            raise ResourceNotFound("email or password is incorrect")

        return db_user

    async def profile(self, user: User):
        statement = select(User)
        result = await self.session.execute(statement)
        return result.scalars().all()
