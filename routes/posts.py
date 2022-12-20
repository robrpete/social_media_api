from fastapi import APIRouter

router = APIRouter(
    tags=["Post Routes"]
)


@router.get("/posts")
async def get_posts():
    return {"posts": "all posts"}


@router.get("/posts/{user}")
async def get_posts(user: str):
    return {"posts": f"{user} posts"}
