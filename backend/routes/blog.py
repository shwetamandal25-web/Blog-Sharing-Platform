from fastapi import APIRouter
from controller.blog_controller import (
    create_blog,
    get_blogs,
    get_blog,
    update_blog,
    delete_blog
)

router = APIRouter()


# Create Blog
@router.post("/blogs")
def create_blog_route(title: str, content: str, user_id: int):
    return create_blog(title, content, user_id)


# Get All Blogs
@router.get("/blogs")
def get_all_blogs():
    return get_blogs()


# Get One Blog
@router.get("/blogs/{blog_id}")
def get_single_blog(blog_id: int):
    return get_blog(blog_id)


# Update Blog
@router.put("/blogs/{blog_id}")
def update_blog_route(blog_id: int, title: str, content: str):
    return update_blog(blog_id, title, content)


# Delete Blog
@router.delete("/blogs/{blog_id}")
def delete_blog_route(blog_id: int):
    return delete_blog(blog_id)