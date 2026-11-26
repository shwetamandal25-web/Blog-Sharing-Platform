import psycopg

def getConnection():
    try:
        conn = psycopg.connect(
            host="localhost",
            dbname="blogify",
            user="bloguser",
            password="blog123",
            port=5432
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None