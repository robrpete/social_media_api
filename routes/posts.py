from fastapi import APIRouter, HTTPException
from models import Post
from database import (
    create_post,
    edit_post,
    get_user_posts,
)

router = APIRouter(
    tags=["Post Routes"]
)


@router.post("/post/create", response_model=Post)
async def create_post_(post: Post):
    response = await create_post(post.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")


@router.post("/post/edit", response_model=Post)
async def edit_post_(username: str, password: str, content):
    response = await edit_post(username, password, content)
    return response


@router.get('/user/posts')
async def get_user_posts_(username: str, password: str):
    response = await get_user_posts(username, password)
    return response
