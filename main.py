
from fastapi import FastAPI
from database import engine, Base
import models
from utils import encode_base62
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi import Depends
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "URL Shortener API is running!"}

@app.get("/test/{number}")
def test(number: int):
    return {"short_code": encode_base62(number)}
@app.post("/shorten")
def create_short_url(original_url: str, db: Session = Depends(get_db)):
    
    
    new_url = models.URL(original_url=original_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    
    short_code = encode_base62(new_url.id)

    
    new_url.short_code = short_code
    db.commit()

    return {
        "original_url": original_url,
        "short_url": f"http://127.0.0.1:8000/r/{short_code}"
    }
@app.get("/r/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):

    url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if url:
        return RedirectResponse(url.original_url)
    else:
        return {"error": "URL not found"}
