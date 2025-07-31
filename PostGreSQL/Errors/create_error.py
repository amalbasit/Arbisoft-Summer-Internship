import psycopg2
import logging


logging.basicConfig(
    filename='create_error.log',
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
                # Intentionally wrong SQL - Missing comma between columns
                cur.execute(
                    '''
                    CREATE TABLE Books (
                        id SERIAL PRIMARY KEY 
                        title varchar(100),
                        author varchar(100),
                        genre varchar(50),
                        price int,
                        stock int
                    );
                    '''
                )
                logging.info("Table 'Books' created successfully.")

            except Exception as e:
                logging.error(f"[ERROR] Table creation failed: {e}")

                # Undo uncommited changes
                conn.rollback()

                # Fixing the error with correct SQL
                cur.execute("DROP TABLE IF EXISTS Books;") 
                cur.execute(
                    '''
                    CREATE TABLE Books (
                        id SERIAL PRIMARY KEY,
                        title varchar(100),
                        author varchar(100),
                        genre varchar(50),
                        price int,
                        stock int
                    );
                    '''
                )
                logging.info("[FIXED] Table 'Books' created successfully after fixing SQL syntax.")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    if conn is not None:
        conn.close()