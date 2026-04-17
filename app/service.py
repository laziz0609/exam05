from datetime import datetime


from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import Book
from .schemas import CreateBook, UpdateBook



def get_all_books(db: Session) -> list[Book]:
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, create_book: CreateBook) -> Book:
    book = Book(
        title=create_book.title,
        author=create_book.author,
        genre=create_book.genre,
        year=create_book.year,
        rating=create_book.rating,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def update_book(db: Session, book_id: int, updated_book: UpdateBook) -> Book | None:
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = updated_book.title or book.title
    book.author = updated_book.author or book.author
    book.genre = updated_book.genre or book.genre
    book.year = updated_book.year or book.year
    book.rating = updated_book.rating or book.rating
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int) -> bool:
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return True


def search_books(db: Session, query: str) -> list[Book]:
    return db.query(Book).filter(
        (Book.title.ilike(f"%{query}%")) |
        (Book.author.ilike(f"%{query}%"))
    ).all()


def filter_book_by_year(db: Session, min_year: int | None, max_year: int | None) -> list[Book]:

    start_date = min_year if min_year else 1
    end_date = max_year if max_year else datetime.now().year
    return db.query(Book).filter(
        Book.year.between(start_date, end_date)
    ).all()