from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

from .database import Base

from datetime import date

import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

class User(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    foto = Column(String)
    postagens = relationship("Post", back_populates="autor")

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError("Email address cannot be empty")
        if not is_valid_email(email):
            raise ValueError("Invalid email address format")
        return email

    __table_args__ = (
        CheckConstraint("LENGTH(nome) >= 3", name='check_nome_length'),
    )



class Post(Base):
    __tablename__ = "postagem"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    texto = Column(String, nullable=False)
    data = Column(Date, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    autor = relationship("User", back_populates="postagens")
    tema_id = Column(Integer, ForeignKey('tema.id'))
    tema = relationship("Theme", back_populates="postagens")

    __table_args__ = (
        CheckConstraint("LENGTH(titulo) >= 5", name='check_titulo_length'),
        CheckConstraint("LENGTH(texto) >= 10", name='check_texto_length'),
    )


class Theme(Base):
    __tablename__ = "tema"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    postagens = relationship("Post", back_populates="tema") 

    __table_args__ = (
        CheckConstraint("LENGTH(descricao) >= 3", name='check_descricao_length'),
    )

print('rodou')