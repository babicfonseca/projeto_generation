from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

from .database import Base
#from database import Base

from datetime import datetime

import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    photo = Column(String)
    posts = relationship("Post", back_populates="author")

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError("Email address cannot be empty")
        if not is_valid_email(email):
            raise ValueError("Invalid email address format")
        return email

    __table_args__ = (
        CheckConstraint("LENGTH(name) >= 3", name='check_name_length'),
    )



class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    data = Column(Date, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="posts")
    theme_id = Column(Integer, ForeignKey('theme.id'))
    theme = relationship("Theme", back_populates="posts")

    __table_args__ = (
        CheckConstraint("LENGTH(title) >= 5", name='check_title_length'),
        CheckConstraint("LENGTH(text) >= 10", name='check_text_length'),
    )


class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    posts = relationship("Post", back_populates="theme") 

    __table_args__ = (
        CheckConstraint("LENGTH(description) >= 3", name='check_description_length'),
    )

print('rodou')