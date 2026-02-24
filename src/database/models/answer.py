from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.database.models.question import Question


class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)

    answer: Mapped[str] = mapped_column(String(256))

    correct: Mapped[bool]

    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    question: Mapped["Question"] = relationship(back_populates="answers")

    def __repr__(self) -> str:
        return f"Answer(id={self.id!r}, answer={self.answer!r}, correct={self.correct!r})"
