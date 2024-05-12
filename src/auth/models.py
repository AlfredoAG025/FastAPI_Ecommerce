from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Table
from sqlalchemy.orm import relationship
from src.database import Base

role_permission_association = Table(
    'role_permission',
    Base.metadata,
    Column('role_id',Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id',Integer, ForeignKey('permissions.id'), primary_key=True)
)


class Role(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    
    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", secondary=role_permission_association, back_populates="roles")


class Permission(Base):
    __tablename__ = "permissions"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    
    roles = relationship("Role", secondary=role_permission_association, back_populates="permissions")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    password_hashed = Column(String)
    phone_number = Column(String(10))
    role_id = Column(ForeignKey("roles.id"))
    
    role = relationship("Role", back_populates="users")
    
