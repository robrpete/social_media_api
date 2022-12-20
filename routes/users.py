from fastapi import APIRouter, HTTPException
from models import User
from database import create_user

router = APIRouter(
    tags=["User Routes"]
)


@router.post("/user/create", response_model=User)
async def create_user_(user: User):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")


@router.get("/user/signin")
async def sign_in():
    return {"user": "signed in user"}


@router.get("/user/signout")
async def sign_out():
    return {"user": "signed out"}
