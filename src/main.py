from fastapi import FastAPI
import uvicorn
from database import SessionLocal, engine


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
