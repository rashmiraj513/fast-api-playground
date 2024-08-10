from fastapi import FastAPI, Path, Query, HTTPException
from Book import BookRequest, Book, books_arr, find_book_id
from starlette import status

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all_books():
    return "Welcome to the Books API"


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return books_arr


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in books_arr:
        if book.id == book_id:
            return book

    # If no book found
    raise HTTPException(status_code=404, detail="Item not found...")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in books_arr:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_books_by_publish_date(publish_date: int = Query(gt=1998, lt=2031)):
    books_to_return = []
    for book in books_arr:
        if book.publised_date == publish_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    print(book_request)
    new_book = Book(**book_request.model_dump())
    books_arr.append(find_book_id(new_book))


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_updated = False
    for i in range(len(books_arr)):
        if books_arr[i].id == book.id:
            books_arr[i] = Book(**book.model_dump())
            book_updated = True
            break

    # If no book found
    if not book_updated:
        raise HTTPException(status_code=404, detail="Item not found...")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(books_arr)):
        if books_arr[i].id == book_id:
            books_arr.pop(i)
            book_deleted = True
            break

    # If no book found
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found...")
