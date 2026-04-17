from typing import Annotated, Optional
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class CreateBook(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=255)]
    author: Annotated[str, Field(min_length=1, max_length=255)]
    genre: Annotated[str, Field(min_length=1, max_length=255)]
    year: Annotated[int, Field(ge=1, le=datetime.now().year+1)]
    rating: Annotated[float, Field(ge=0.0, le=5.0)]


class UpdateBook(BaseModel):
    title: Optional[Annotated[str | None, Field(min_length=1, max_length=255)]] = None
    author: Optional[Annotated[str | None, Field(min_length=1, max_length=255)]] = None
    genre: Optional[Annotated[str | None, Field(min_length=1, max_length=255, default=None)]] = None
    year: Optional[Annotated[int | None, Field(ge=1, le=datetime.now().year+1, default=None)]] = None
    rating: Optional[Annotated[float | None, Field(ge=0.0, le=5.0, default=None)]] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int
    rating: float

    model_config = ConfigDict(from_attributes=True)