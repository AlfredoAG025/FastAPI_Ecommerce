from fastapi import APIRouter, Depends

from src.middlewares import JWTBearer

from .dependencies import get_db
from . import schemas, service, models
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register/", tags=["auth"], response_model=schemas.UserSchema)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.register(db=db, user=user)

@router.post("/login/", tags=["auth"])
async def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    user = service.login(db=db, user=user)
    if user:
        return user
    return "Email Or Password Incorrect!"
    

@router.get("/users/", tags=["users"], response_model=list[schemas.UserSchema])
async def read_users(db: Session = Depends(get_db)):
    return service.get_users(db=db)



@router.get("/roles/", tags=["roles"], response_model=list[schemas.RoleSchema], dependencies=[Depends(JWTBearer())])
async def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = service.get_roles(db, skip=skip, limit=limit)
    return roles
