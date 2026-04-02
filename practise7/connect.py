import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "phonebook_db",
    "user": "postgres",
    "password": "12345678",
    "port": 5432
}

def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            port=DB_CONFIG["port"]
        )
        return conn
    except Exception as e:
        print(f"[ERROR] Could not connect to database: {e}")
        raise