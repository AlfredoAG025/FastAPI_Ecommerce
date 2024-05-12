from jwt import encode, decode
import os
from dotenv import load_dotenv
import bcrypt

load_dotenv()

secret_key = os.getenv("SECRET_KEY")


def create_token(data: dict) -> str:
    token: str = encode(
        payload=data,
        key=secret_key,
        algorithm="HS256"
    )
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, secret_key, ["HS256"])
    return data
    

def hash_plain_password(password: bytes):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password

def verify_password(input_password: bytes, hashed_password: bytes):
    return bcrypt.checkpw(input_password, hashed_password)