from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class PostBase(BaseModel):
    title: str
    text: str | None = None
    #theme_id: int


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    data: date
    user_id: int
    theme_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    photo: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    post: List[Post] = []

    class Config:
        orm_mode = True


class ThemeBase(BaseModel):
    description: str


class ThemeCreate(ThemeBase):
    pass


class Theme(ThemeBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True