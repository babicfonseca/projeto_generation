from sqlalchemy.orm import Session

from . import models, schemas
#import models, schemas

# CRUD User
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, name=user.name, photo=user.photo)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, old_user: schemas.UserCreate, new_user_data: schemas.UserCreate):
    old_user.name = new_user_data.name
    old_user.email = new_user_data.email
    old_user.photo = new_user_data.photo
    db.commit()
    db.refresh(old_user)
    return

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db=db, user_id=user_id)
    db.delete(user)
    db.commit()
    return



# CRUD Theme
def create_theme(db: Session, theme: schemas.ThemeCreate):
    db_theme = models.Theme(description=theme.description)
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme

def get_theme(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Theme).offset(skip).limit(limit).all()

def get_theme_by_id(db: Session, theme_id: int):
    return db.query(models.Theme).filter(models.Theme.id == theme_id).first()

def update_theme(db: Session, theme_id: schemas.ThemeCreate, new_theme_data: schemas.ThemeCreate):
    theme_id.description = new_theme_data.description
    db.commit()
    db.refresh(theme_id)
    return

def delete_theme(db: Session, theme_id: int):
    theme = db.query(models.Theme).filter(models.Theme.id == theme_id).first()
    db.delete(theme)
    db.commit()
    return



# CRUD Post
def get_post(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def create_user_post(db: Session, post: schemas.PostCreate, user_id: int, theme_id: int):
    db_post = models.Post(title=post.title, text=post.text, theme_id=theme_id, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: schemas.PostCreate, new_post_data: schemas.PostCreate):
    post_id.title = new_post_data.title
    post_id.text = new_post_data.text
    db.commit()
    db.refresh(post_id)
    return

def delete_post(db: Session, post_id: int):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    db.delete(post)
    db.commit()
    return