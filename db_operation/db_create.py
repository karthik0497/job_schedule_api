import psycopg2
from psycopg2 import sql, OperationalError
from urllib.parse import urlparse

# Define the new database name and table name
db_name = "new_database"
table_name = "jobs"
# Define your connection strings
DATABASE_URL = "postgresql://karthik:VojIUmRXZArEPv6eevaLkDMP4VuypWOT@dpg-cqgd43dds78s73ccrk20-a.singapore-postgres.render.com/job_schedule_db"
parsed_url = urlparse(DATABASE_URL)

def create_db():
    conn = None
    try:
        # Connect to the PostgreSQL server using the postgres database
        conn = psycopg2.connect(
            dbname='postgres',
            user=parsed_url.username,
            password=parsed_url.password,
            host=parsed_url.hostname,
            port=parsed_url.port
        )
        conn.autocommit = True  # Needed for CREATE DATABASE command

        with conn.cursor() as cursor:
            # Check if the database already exists
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
            exists = cursor.fetchone()

            if not exists:
                # Create a new database if it does not exist
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
                print(f"Database '{db_name}' created successfully.")
            else:
                print(f"Database '{db_name}' already exists.")

    except OperationalError as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()


def create_table(table_name):
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        with conn.cursor() as cursor:
            # Create the table if it does not exist
            cursor.execute(sql.SQL("""
                CREATE TABLE IF NOT EXISTS {} (
                    job_id SERIAL PRIMARY KEY, 
                    job_name VARCHAR(255) NOT NULL,
                    job_schedule VARCHAR(255) NOT NULL,
                    job_description TEXT NOT NULL,
                    job_type VARCHAR(50),
                    job_params JSONB,
                    last_run TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """).format(sql.Identifier(table_name)))
            conn.commit()
            print(f"Table '{table_name}' created successfully.")
    except OperationalError as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_db()
    create_table(table_name)
    exit(0)
