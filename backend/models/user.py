from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str 
@router.post("/register")
def register_user(user: User):
    print(user.name)
    print(user.email)
    print(user.password)

    return {
        "message": "User registered successfully"
    }