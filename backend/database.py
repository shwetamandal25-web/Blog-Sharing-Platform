from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import psycopg

app = FastAPI()
def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="blogify",
        user="postgres",
        password="blogify123"
    )


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

class User(BaseModel):
    name: str
    email: EmailStr
    password: str


@app.on_event("startup")
def startup():
    create_table()



@app.get("/")
def home():
    return {"message": "Welcome to Blogify API"}


@app.post("/register")
def register_user(user: User):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (name, email, password)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (user.name, user.email, user.password)
        )

        user_id = cursor.fetchone()[0]
        conn.commit()

        return {
            "message": "User registered successfully",
            "user_id": user_id
        }

    except Exception:
        conn.rollback()
        raise HTTPException(
            status_code=400,
            detail="Registration failed. Email may already exist."
        )

    finally:
        cursor.close()
        conn.close()


@app.get("/users")
def get_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email FROM users")

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }
        for user in users
    ]