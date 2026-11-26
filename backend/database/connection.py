import psycopg

def getConnection():
    conn = psycopg.connect(
        host="localhost",
        dbname="blogify",
        user="bloguser",
        password="blog123",
        port=5432
    )
    return conn