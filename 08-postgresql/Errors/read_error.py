import psycopg2
import logging

logging.basicConfig(
    filename='read_error.log',
    filemode='w',
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - Line: %(lineno)d - %(message)s'
)

conn = None

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
                # Intentionally wrong SQL - Incorrect Syntax
                cur.execute(
                    '''
                        SELECT title, price 
                        FROM Books
                        WHERE title IS LIKE T% AND price < 20;
                    '''
                )
                logging.info("Query ran successfully.")

            except Exception as e:
                logging.error(f"Query failed: {e}")

                # Undo uncommited changes
                conn.rollback()

                # Fixing the error with correct SQL
                cur.execute(
                    '''
                        SELECT title, price 
                        FROM Books
                        WHERE title LIKE 'T%' AND price < 20;
                    '''
                )
                for data in cur.fetchall():
                    print(data)

                logging.info("Query ran successfully after fixing SQL syntax.")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    if conn is not None:
        conn.close()