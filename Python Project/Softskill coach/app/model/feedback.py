from sqlalchemy import Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.db_config import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(primary_key=True)

    grammar_score: Mapped[float] = mapped_column(Float)

    confidence_score: Mapped[float] = mapped_column(Float)

    vocabulary_score: Mapped[float] = mapped_column(Float)

    suggestions: Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="feedbacks"
    )