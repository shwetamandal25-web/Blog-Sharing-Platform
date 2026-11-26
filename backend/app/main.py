from fastapi import FastAPI

from database.connection import Base, engine
from models import user  # noqa: F401  (so the table gets created)
from routes import auth
from router.blog import router as blog_router
from router.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog Sharing Platform")
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Blog Sharing Platform API"}

