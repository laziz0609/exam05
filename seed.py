from sqlalchemy.orm import Session

from app.database import engine
from app.models import Book

def seed_books():
    books = [
        Book(
            title="Clean Code",
            author="Robert C. Martin",
            genre="Programming",
            year=2008,
            rating=4.7
        ),
        Book(
            title="The Pragmatic Programmer",
            author="Andrew Hunt",
            genre="Programming",
            year=1999,
            rating=4.6
        ),
        Book(
            title="Atomic Habits",
            author="James Clear",
            genre="Self-help",
            year=2018,
            rating=4.8
        ),
        Book(
            title="1984",
            author="George Orwell",
            genre="Dystopian",
            year=1949,
            rating=4.5
        ),
        Book(
            title="To Kill a Mockingbird",
            author="Harper Lee",
            genre="Classic",
            year=1960,
            rating=4.4
        ),
    ]

    with Session(engine) as session:
        session.add_all(books)
        session.commit()

    print("✅ Bazaga demo datalar qo'shildi!")


