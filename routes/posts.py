from fastapi import APIRouter, HTTPException
from models import Post
from database import create_post

router = APIRouter(
    tags=["Post Routes"]
)


@router.post("/post/create", response_model=Post)
async def create_post_(post: Post):
    response = await create_post(post.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")
