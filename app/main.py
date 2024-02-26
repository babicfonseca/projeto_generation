from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

#import crud, models, schemas
#from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

description="""
This API helps you to Create, Read, Update and Delete (CRUD) data users, posts, themes in a database.

## User

You can:

* **Create users**
* **Search users**
* **Update users data**
* **Delete users**


## Post

You can:

* **Create posts**
* **Search posts**
* **Update posts data**
* **Delete posts**


## Theme

You can:

* **Create themes**
* **Search themes**
* **Update themes**
* **Delete themes**
"""

app = FastAPI(
    title="Generation Final Project - AWS Course",
    description=description,
    version= "0.0.1",
    contact={
        "name": "Bárbara Fonseca",
        "github": "https://github.com/babicfonseca",
        "email": "cfonseca.barbara@gmail.com",
        "linkedin": "https://www.linkedin.com/in/barbaracfonseca/",
    },
    license_info={
        "name": "MIT License",
    },
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, new_user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, old_user=db_user, new_user_data=new_user_data)

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id=user_id)


#Theme
@app.post("/theme/", response_model=schemas.Theme)
def create_theme(
    theme: schemas.ThemeCreate, db: Session = Depends(get_db)
):
    return crud.create_theme(db=db, theme=theme)


@app.get("/theme/", response_model=list[schemas.Theme])
def read_theme(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    theme = crud.get_theme(db, skip=skip, limit=limit)
    return theme

@app.put("/theme/{theme_id}", response_model=schemas.Theme)
def update_theme(theme_id: int, new_theme_data: schemas.ThemeCreate, db: Session = Depends(get_db)):
    db_theme = crud.get_theme_by_id(db, theme_id=theme_id)
    if db_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return crud.update_theme(db, theme_id=db_theme, new_theme_data=new_theme_data)

@app.delete("/theme/{theme_id}", response_model=schemas.Theme)
def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    return crud.delete_theme(db, theme_id=theme_id)


# Post
@app.post("/users/{user_id}/{theme_id}/post/", response_model=schemas.Post)
def create_post_for_user(
    user_id: int, theme_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)
):
    return crud.create_user_post(db=db, post=post, user_id=user_id, theme_id=theme_id)


@app.get("/post/", response_model=list[schemas.Post])
def read_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_post(db, skip=skip, limit=limit)
    return posts

@app.put("/post/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, new_post_data: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.get_post_by_id(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.update_post(db, post_id=db_post, new_post_data=new_post_data)


@app.delete("/post/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return crud.delete_post(db, post_id=post_id)