from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.db_config import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    conversations = relationship(
        "Conversation",
        back_populates="user"
    )

    feedbacks = relationship(
        "Feedback",
        back_populates="user"
    )