from pydantic import BaseModel, EmailStr
from datetime import date, time
from typing import Optional


class User(BaseModel):
    username: str
    password: str
    email: str = None
    last_seen: str = None


class Post(BaseModel):
    user: User
    content: str
    created: str
    likes: Optional[int] = None
    comment: Optional[str] = None
