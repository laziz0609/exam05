from typing import Annotated 
from datetime import datetime

from fastapi import APIRouter, Depends, Path, HTTPException, Query

from ..service import (
    get_all_books,
    get_book_by_id,
    create_book,
    update_book,
    delete_book,
    search_books,
    filter_book_by_year
)
from ..database import get_session
from ..schemas import CreateBook, UpdateBook, BookResponse

router = APIRouter(prefix="/api/v1/books", tags=["Books"])


@router.get("/all", response_model=list[BookResponse])
def get_all_books_view(session=Depends(get_session)):
    return get_all_books(session)

@router.get("/search", response_model=list[BookResponse])
def search_books_view(
    search: Annotated[str, Query(min_length=1)],
    session=Depends(get_session)
):
    return search_books(session, search)

@router.get("/filter", response_model=list[BookResponse])
def filter_books_by_year_view(
    min_year: Annotated[int | None, Query(ge=1)] = None,
    max_year: Annotated[int | None, Query(ge=1, le=datetime.now().year)] = None,
    session=Depends(get_session)
):
    return filter_book_by_year(session, min_year, max_year)

@router.get("/{book_id}", response_model=BookResponse)
def get_book_by_id_view(
    book_id: Annotated[int, Path(ge=1)],
    session=Depends(get_session)
):
    book = get_book_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book_view(
    book_id: Annotated[int, Path(ge=1)],
    updated_book: UpdateBook,
    session=Depends(get_session)
):
    book = update_book(session, book_id, updated_book)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}", status_code=204)
def delete_book_view(
    book_id: Annotated[int, Path(ge=1)],
    session=Depends(get_session)
):
    delete_book(session, book_id)
    return {"detail": "Book deleted successfully"}

@router.post("/create", response_model=BookResponse, status_code=201)
def create_book_view(
    create_book_: CreateBook,
    session=Depends(get_session)
):
    return create_book(session, create_book_)