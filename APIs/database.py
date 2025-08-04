import os
from dotenv import load_dotenv
import psycopg2

# Load variables from .env file
load_dotenv()

def get_connection():
    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# Example usage:
if __name__ == "__main__":
    conn = get_connection()
    print("Connected successfully!")
    conn.close()
