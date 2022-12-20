from fastapi import APIRouter

router = APIRouter(
    tags=["User Routes"]
)


@router.post("/user/create")
async def create_user():
    return {"created": "user"}


@router.get("/user/signin")
async def sign_in():
    return {"user": "signed in user"}


@router.get("/user/signout")
async def sign_out():
    return {"user": "signed out"}
