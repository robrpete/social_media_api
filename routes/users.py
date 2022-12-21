from fastapi import APIRouter, HTTPException
from models import User
from database import (
    create_user,
    get_user,
    sign_out_user,
)

router = APIRouter(
    tags=["User Routes"]
)


@router.post("/user/create", response_model=User)
async def create_user_(user: User):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")


@router.get("/user/signin", response_model=User)
async def sign_in(username: str, password: str):
    response = await get_user(username, password)
    if response:
        return response
    raise HTTPException(400, "Bad Request")


@router.get("/user/signout", response_model=User)
async def sign_out(username: str, password: str):
    response = await sign_out_user(username, password)
    if response:
        return response
    raise HTTPException(400, "Bad Request")
