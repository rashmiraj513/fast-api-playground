from typing import Optional
from pydantic import BaseModel, Field


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    publised_date: int

    def __init__(self, id, title, author, description, rating, publised_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publised_date = publised_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    publised_date: int = Field(gt=1998, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The song of Ice and Fire",
                "author": "George R. R. Martin",
                "description": "My favorite book",
                "rating": 5,
                "published_date": 2021,
            }
        }
    }


books_arr = [
    Book(1, "Computer Science Pro", "Author 5", "A very nice book!", 5, 2030),
    Book(2, "Be Fast with FastAPI", "Author 5", "A great book!", 5, 2030),
    Book(3, "Master Endpoints", "Author 5", "A awesome book!", 5, 2029),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2028),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2027),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2026),
]


def find_book_id(book: Book):
    book.id = 1 if len(books_arr) == 0 else books_arr[-1].id + 1
    return book
