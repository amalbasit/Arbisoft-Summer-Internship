import psycopg2
import logging

logging.basicConfig(
    filename='delete_error.log',
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
                # Intentionally wrong SQL
                cur.execute(
                    '''
                        DELETE FROM Books TABLE
                        WHERE price > 25;
                    '''
                )
                logging.info("Deletion was successful.")

            except Exception as e:
                logging.error(f"[ERROR] Deletion unsuccessful: {e}")

                # Undo uncommited changes
                conn.rollback()

                # Fixing the error with correct SQL
                cur.execute(
                    '''
                        DELETE FROM Books
                        WHERE price > 25;
                    '''
                )

                cur.execute(
                """
                    SELECT title, price
                    FROM Books
                    WHERE price > 25
                """
                )
            
                rows = cur.fetchall()

                if not rows:
                    print("All books with price greater than 25 were deleted.\n")
                else:
                    for row in rows:
                        print(row) 

                logging.info("[FIXED] All books with price above 25 were deleted.")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    if conn is not None:
        conn.close()