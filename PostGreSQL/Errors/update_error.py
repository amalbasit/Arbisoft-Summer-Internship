import psycopg2
import logging

logging.basicConfig(
    filename='update_error.log',
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
                # Intentionally wrong SQL - incorrect syntax to increment value
                cur.execute(
                    '''
                        UPDATE Books
                        SET stock += 100
                        WHERE genre = 'Fantasy';
                    '''
                )
                logging.info("Fantasy Books stock updated successfully.")

            except Exception as e:
                logging.error(f"[ERROR] Incorrect increment syntax: {e}")

                # Undo uncommited changes
                conn.rollback()

                # Fixing the error with correct SQL
                cur.execute(
                """
                    UPDATE Books
                    SET stock = stock + 100
                    WHERE genre = 'Fantasy';
                """
                )
                cur.execute(
                    """
                        SELECT title, stock
                        FROM Books
                        WHERE genre = 'Fantasy';
                    """
                )
                for data in cur.fetchall():
                    print(data)
                logging.info("[FIXED] Fantasy Books stock updated successfully after fixing SQL syntax.")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    if conn is not None:
        conn.close()