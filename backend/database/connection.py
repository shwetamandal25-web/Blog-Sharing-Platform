import psycopg
def getConnection ():
    conn = psycopg.connect(
        DB_HOST=localhost
        DB_NAME=blogify
        DB_USER=bloguser
        DB_PASSWORD=blog123
        DB_PORT=5432
    )
    return conn