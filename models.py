from pydantic import BaseModel, EmailStr
from datetime import date, time
from typing import Optional


class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    last_seen: Optional[list[date, time]] = None


class Post(BaseModel):
    user: User
    content: str
    created: date
    likes: Optional[int] = None
    comment: Optional[str] = None
