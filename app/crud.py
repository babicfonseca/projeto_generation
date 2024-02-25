from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_post(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_user_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), usuario_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_theme(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Theme).offset(skip).limit(limit).all()

def create_user_theme(db: Session, theme: schemas.ThemeCreate, tema_id: int):
    db_theme = models.Theme(**theme.dict(), theme_id=tema_id)
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme