from datetime import datetime
from typing import Union
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str
    description: Union[str, None] = None


class RoleSchema(RoleBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str


class UserLogin(UserBase):
    password: str

class UserCreate(UserLogin):
    name: str
    lastname: str
    phone_number: str
    

class UserSchema(UserBase):
    id: int
    role: RoleSchema = None
    
    class Config:
        orm_mode = True

