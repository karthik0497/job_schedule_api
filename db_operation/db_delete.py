import psycopg2
from psycopg2 import sql, OperationalError

# Define the new database name
db_name = "new_database"
table_name = "jobs"
# Define your connection strings
conn_str = "postgresql://karthik:VojIUmRXZArEPv6eevaLkDMP4VuypWOT@dpg-cqgd43dds78s73ccrk20-a.singapore-postgres.render.com/job_schedule_db?sslmode=require"
DATABASE_URL = f"postgresql://karthik:VojIUmRXZArEPv6eevaLkDMP4VuypWOT@dpg-cqgd43dds78s73ccrk20-a.singapore-postgres.render.com/{db_name}?sslmode=require"


def create_db():
    conn = None
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(conn_str)
        conn.autocommit = True  # Needed for CREATE DATABASE command

        with conn.cursor() as cursor:
            # Check if the database already exists
            cursor.execute("""
                SELECT 1 FROM pg_database WHERE datname = %s
            """, (db_name,))
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
