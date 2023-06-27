from fastapi import HTTPException
from fastapi import status

from core.hashing import Hasher
from db.models.roles import Role
from db.models.users import User
from schemas.users import UserCreate, UserUpdate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    role = db.query(Role).filter(Role.name == user.role).first()
    if role is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found role with name is %s".format(user.role)
        )
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
        fullname=user.fullname,
        role=role.name
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user


def list_user(db: Session):
    users = db.query(User).all()
    return users


def update_user_by_id(id: int, user: UserUpdate, db: Session):
    existing_user = db.query(User).filter(User.id == id).first()
    if not existing_user:
        return 0
    if user.fullname is not None:
        existing_user.fullname = user.fullname
    if user.email is not None:
        existing_user.email = user.email
    if user.role is not None:
        existing_role = db.query(Role).filter(Role.name == user.role).first()
        if not existing_role:
            return 0
        else:
            existing_user.role_id = existing_role.id
    existing_user.update()
    db.commit()
    return 1


def block_user_by_id(id: int, db: Session):
    existing_user = db.query(User).filter(User.id == id).first()
    if not existing_user:
        return 0
    existing_user.is_active = False
    existing_user.update()
    db.commit()
    return 1


def active_user_by_id(id: int, db: Session):
    existing_user = db.query(User).filter(User.id == id).first()
    if not existing_user:
        return 0
    existing_user.is_active = True
    existing_user.update()
    db.commit()
    return 1
