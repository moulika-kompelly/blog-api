from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Home route
@app.get("/")
def home():
    return {"message": "Blog API Running"}

# Create blog
@app.post("/blogs")
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=blog.title,
        content=blog.content
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog
# Get all blogs
@app.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()

# Get single blog
@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(
        models.Blog.id == blog_id
    ).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    return blog
# Update blog
@app.put("/blogs/{blog_id}")
def update_blog(
    blog_id: int,
    blog: schemas.BlogCreate,
    db: Session = Depends(get_db)
):
    db_blog = db.query(models.Blog).filter(
        models.Blog.id == blog_id
    ).first()

    if not db_blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    db_blog.title = blog.title
    db_blog.content = blog.content

    db.commit()
    db.refresh(db_blog)

    return db_blog

# Delete blog
@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(
        models.Blog.id == blog_id
    ).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    db.delete(blog)
    db.commit()

    return {"message": "Blog deleted"}
