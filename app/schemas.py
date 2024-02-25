from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class PostBase(BaseModel):
    titulo: str
    texto: str | None = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    data: date
    usuario_id: int
    tema_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    nome: str
    email: str
    foto: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    postagem: list[Post] = []

    class Config:
        orm_mode = True


class ThemeBase(BaseModel):
    descricao: str


class ThemeCreate(ThemeBase):
    pass


class Theme(ThemeBase):
    id: int
    postagens: List[Post] = []

    class Config:
        orm_mode = True