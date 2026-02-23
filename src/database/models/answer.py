from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base
from src.database.models.question import Question


class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)

    answer: Mapped[str] = mapped_column(String(256))

    correct: Mapped[bool]

    question: Mapped["Question"] = relationship(
        back_populates="answer", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Answer(id={self.id!r}, answer={self.answer!r}, correct={self.correct!r})"
