from fastapi import FastAPI
from routes.auth import router as auth_router

app = FastAPI(
    title="Blog Sharing Platform",
    description="Backend API for Blog Sharing Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Blog Sharing Platform"
    }


@app.get("/about")
def about():
    return {
        "message": "This is the Blog Sharing Platform API"
    }


app.include_router(auth_router)

