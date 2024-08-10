from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/")
async def root():
    return {"message": "Welcome to the Book Library API"}


@app.get("/books")
async def read_all_books():
    return BOOKS


# # FastAPI reads functions in chronological order (Static Parameter)
@app.get("/books/mybook")
async def read_all_books():
    return {"book_title": "My favorite book"}


# # Dynamic Parameter
@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# Query Parameter
@app.get("/books/")
async def read_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    print(books_to_return)
    return books_to_return


# Dynamic Parameter along with Query Parameter
@app.get("/books/{book_author}/")
async def ready_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book
            break


@app.delete("/book/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


# Assignment: Create a new API endpoint that can fetch all books from a specific author using either path parameters or, query parameters.
# To run these, comment above route which uses path parameters and query parameters


# Assignment Solution using Path Parameters
@app.get("/books/{book_author}")
async def get_books_by_author(book_author: str):
    books_by_author = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            books_by_author.append(book)
    return books_by_author


# Assignment Solution using Query Parameters
@app.get("/books/")
async def read_books_by_author(author: str):
    books_by_author = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_by_author.append(book)
    return books_by_author
