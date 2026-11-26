from schema.user import UserCreate


def register_user(user: UserCreate):
    return {
        "message": "User registered successfully",
        "username": user.username,
        "email": user.email
    }