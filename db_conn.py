#db-conn.py

import psycopg2,os
from typing import Generator

DATABASE_URL = os.getenv('DATABASE_URL')
def get_db_connection() -> Generator:
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()