from fastapi import APIRouter
from database import getConnection

router = APIRouter()


# CREATE BLOG
@router.post("/blogs")
def create_blog(title: str, content: str, user_id: int):

    conn = getConnection()
    cursor = conn.cursor()

    query = """
        INSERT INTO blogs (title, content, user_id)
        VALUES (%s, %s, %s)
        RETURNING id
    """

    cursor.execute(query, (title, content, user_id))

    blog_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Blog created successfully",
        "blog_id": blog_id
    }


# GET ALL BLOGS
@router.get("/blogs")
def get_blogs():

    conn = getConnection()
    cursor = conn.cursor()

    query = """
        SELECT id, title, content, user_id
        FROM blogs
        ORDER BY id DESC
    """

    cursor.execute(query)

    blogs = cursor.fetchall()

    cursor.close()
    conn.close()

    result = []

    for blog in blogs:
        result.append({
            "id": blog[0],
            "title": blog[1],
            "content": blog[2],
            "user_id": blog[3]
        })

    return result


# GET ONE BLOG
@router.get("/blogs/{blog_id}")
def get_blog(blog_id: int):

    conn = getConnection()
    cursor = conn.cursor()

    query = """
        SELECT id, title, content, user_id
        FROM blogs
        WHERE id = %s
    """

    cursor.execute(query, (blog_id,))

    blog = cursor.fetchone()

    cursor.close()
    conn.close()

    if blog is None:
        return {
            "message": "Blog not found"
        }

    return {
        "id": blog[0],
        "title": blog[1],
        "content": blog[2],
        "user_id": blog[3]
    }


# UPDATE BLOG
@router.put("/blogs/{blog_id}")
def update_blog(blog_id: int, title: str, content: str):

    conn = getConnection()
    cursor = conn.cursor()

    query = """
        UPDATE blogs
        SET title = %s,
            content = %s
        WHERE id = %s
    """

    cursor.execute(query, (title, content, blog_id))

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Blog updated successfully"
    }


# DELETE BLOG
@router.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int):

    conn = getConnection()
    cursor = conn.cursor()

    query = """
        DELETE FROM blogs
        WHERE id = %s
    """

    cursor.execute(query, (blog_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Blog deleted successfully"
    }