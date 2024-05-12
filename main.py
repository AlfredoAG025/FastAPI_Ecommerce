from fastapi import FastAPI
import uvicorn
from src.auth.router import router as auth_router

app = FastAPI(
    title="Ecommerce"
)
app.include_router(auth_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
