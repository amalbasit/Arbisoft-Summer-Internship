import psycopg2
import logging

logging.basicConfig(
    filename='insert_error.log',
    filemode='w',
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - Line: %(lineno)d - %(message)s'
)

conn = None
book_values = [
                ('The Silent Patient', 'Alex Michaelides', 'Thriller', 15, 120),
                ('Educated', 'Tara Westover', 'Memoir', 20, 75),
                ('Becoming', 'Michelle Obama', 'Biography', 25, 80),
                ('Where the Crawdads Sing', 'Delia Owens', 'Fiction', 18, 150),
                ('Normal People', 'Sally Rooney', 'Romance', 14, 60),
                ('The Testaments', 'Margaret Atwood', 'Dystopian', 22, 45),
                ('Circe', 'Madeline Miller', 'Fantasy', 19, 90),
                ('The Night Circus', 'Erin Morgenstern', 'Fantasy', 17, 55),
                ('Sapiens', 'Yuval Noah Harari', 'History', 30, 40),
                ('Homo Deus', 'Yuval Noah Harari', 'Philosophy', 28, 30),
                ('Atomic Habits', 'James Clear', 'Self-help', 16, 110),
                ('Thinking, Fast and Slow', 'Daniel Kahneman', 'Psychology', 20, 70),
                ('Dune', 'Frank Herbert', 'Science Fiction', 22, 85),
                ('1984', 'George Orwell', 'Dystopian', 12, 130),
                ('To Kill a Mockingbird', 'Harper Lee', 'Classic', 14, 100),
                ('Pride and Prejudice', 'Jane Austen', 'Classic', 13, 90),
                ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 15, 75),
                ('Moby Dick', 'Herman Melville', 'Classic', 18, 40),
                ('The Catcher in the Rye', 'J.D. Salinger', 'Classic', 14, 60),
                ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 20, 95),
                ('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'Fantasy', 25, 200),
                ('The Alchemist', 'Paulo Coelho', 'Fiction', 16, 120),
                ('The Road', 'Cormac McCarthy', 'Post-apocalyptic', 17, 50),
                ('The Book Thief', 'Markus Zusak', 'Historical Fiction', 18, 65),
                ('Gone Girl', 'Gillian Flynn', 'Thriller', 16, 85),
                ('The Da Vinci Code', 'Dan Brown', 'Thriller', 15, 110),
                ('Angels & Demons', 'Dan Brown', 'Thriller', 15, 100),
                ('Inferno', 'Dan Brown', 'Thriller', 16, 90),
                ('The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Crime', 17, 80)
                ]

try:
    with psycopg2.connect(
        database='Error Demo',
        user='postgres',
        password='admin123',
        host='localhost',
        port='5432'
    ) as conn:

        with conn.cursor() as cur:

            try:
                # Intentionally wrong SQL - placeholders don't match columns
                insert_script = '''
                    INSERT INTO Books (id, title, author, genre, price, stock)
                    VALUES (%s, %s, %s, %s)
                '''

                for data in book_values:
                    cur.execute(insert_script, data)

                logging.info("Data inserted in table 'Books' successfully.")

            except Exception as e:
                logging.error(f"[ERROR] Data insertion failed: {e}")

                # Undo uncommited changes
                conn.rollback()

                # Fixing the error with correct SQL
                insert_script = '''
                    INSERT INTO Books (title, author, genre, price, stock)
                    VALUES (%s, %s, %s, %s, %s)
                '''
                
                for data in book_values:
                    cur.execute(insert_script, data)
              
                logging.info("[FIXED] Data inserted in table 'Books' successfully after fixing SQL syntax.")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    if conn is not None:
        conn.close()