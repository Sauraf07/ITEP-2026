from datetime import date

from src.dao.user_dao import UserDAO
from src.model.user import User

# Create User
user = User(
    name="Saurav",
    email="saurav@gmail.com",
    password="123456",
    phone="9876543210",
    role="customer",
    created_at=date.today(),
    updated_at=date.today()
)

saved_user = UserDAO.save(user)

print("Saved User ID:", saved_user.id)

# Fetch User
db_user = UserDAO.fetch_by_id(saved_user.id)

print(
    db_user.id,
    db_user.name,
    db_user.email,
    db_user.role
)