from sqlalchemy import CheckConstraint, Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base, engine

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    genre: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[float] = mapped_column(Numeric(2, 1), nullable=False)

    __table_args__ = (
        CheckConstraint("rating >= 0 AND rating <= 5", name="rating_range"),
    )

def init_db():
    Base.metadata.create_all(engine)
    print("✅ Bazadagi jadvallar yaratildi!")

def drop_db():
    Base.metadata.drop_all(engine)
    print("✅ Bazadagi jadvallar o'chirildi!")