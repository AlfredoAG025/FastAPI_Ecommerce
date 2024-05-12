from sqlalchemy.orm import Session
from . import models, schemas
from .utils import create_token, hash_plain_password, verify_password


def get_user_by_email(db: Session, email: str):
    user = db.query(models.User).filter_by(email=email).first()
    return user

def login(db: Session, user: schemas.UserLogin):
    user_searched = get_user_by_email(db=db, email=user.email)
    if user_searched:
        if not verify_password(user.password.encode('utf-8'), user_searched.password_hashed.encode('utf-8')):
            return None
        token = create_token(user.model_dump())
        return token
    return None

def register(db: Session, user: schemas.UserCreate):
    CLIENT_ROLE = 2

    hashed_password = hash_plain_password(user.password.encode('utf-8'))
    db_user = models.User(
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        password_hashed=hashed_password.decode('utf-8'),
        phone_number=user.phone_number,
        role_id=CLIENT_ROLE,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()
