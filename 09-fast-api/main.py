from fastapi import FastAPI, HTTPException
from models import Book
from database import get_connection

app = FastAPI()

def get_book_by_query(query, params_tuple):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params_tuple)
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        conn.close()

def format_book_row(result):
    return {
        "id": result[0],
        "title": result[1],
        "author": result[2],
        "year": result[3],
        "price": float(result[4])
    }

@app.post("/books/") # decorator with path parameter (placeholder)
def add_book(book: Book):
    conn = get_connection()
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO books (title, author, year, price)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """
    cursor.execute(insert_query, (book.title, book.author, book.year, book.price))
    book_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Book added", "id": book_id}

@app.get("/books/{book_id}")
def get_book(book_id: int):

    get_query = """
        SELECT *
        FROM books
        WHERE id = %s
    """

    result = get_book_by_query(get_query, (book_id,))

    if result:
        return format_book_row(result)
    else:
        raise HTTPException(status_code=404, detail="Book not found")
    

@app.get('/books/year/{year}')
def get_book_year(year: int):

    get_query = """
        SELECT *
        FROM books
        WHERE year = %s
    """

    result = get_book_by_query(get_query, (year,))

    if result:
        return format_book_row(result)
    else:
        raise HTTPException(status_code=404, detail="Book not found")