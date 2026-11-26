from pydantic import BaseModel


class BlogCreate(BaseModel):
    title: str
    content: str
    user_id: int


class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int