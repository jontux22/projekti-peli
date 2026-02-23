from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base
from src.database.models.answer import Answer


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)

    question: Mapped[str] = mapped_column(String(256))

    difficulty: Mapped[int]

    category: Mapped[str] = mapped_column(String(32))

    answers: Mapped[List["Answer"]] = relationship(
        back_populates="question", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Question(id={self.id!r}, question={self.question!r}, difficulty={self.difficulty!r})"
