from fastapi import FastAPI, HTTPException
from models import Book
from database import get_connection

app = FastAPI()

@app.post("/books/")
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
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return {
            "id": result[0],
            "title": result[1],
            "author": result[2],
            "year": result[3],
            "price": float(result[4])
        }
    else:
        raise HTTPException(status_code=404, detail="Book not found")