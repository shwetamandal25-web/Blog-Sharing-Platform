from database import getConnection


def get_db():
    conn = getConnection()

    try:
        yield conn
    finally:
        conn.close()