from database import getConnection


def register_user(name, email, password):

    conn = getConnection()
    cursor = conn.cursor()

    query = """
        INSERT INTO users (name, email, password)
        VALUES (%s, %s, %s)
        RETURNING id
    """

    cursor.execute(query, (name, email, password))

    user_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "User registered successfully",
        "user_id": user_id
    }


def login_user(email, password):

    conn = getConnection()
    cursor = conn.cursor()

    query = """
        SELECT id, name, email, password
        FROM users
        WHERE email = %s
    """

    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user is None:
        return {
            "message": "User not found"
        }

    if user[3] != password:
        return {
            "message": "Invalid password"
        }

    return {
        "message": "Login successful",
        "user_id": user[0],
        "name": user[1],
        "email": user[2]
    }