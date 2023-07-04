from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.roles import get_role_by_name
from db.repository.users import create_new_user, change_password_repo, update_role_repo
from db.session import get_db
from fastapi import Depends
from schemas.users import ShowUser, UserUpdate
from schemas.users import UserCreate
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException
from fastapi import status

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        user = create_new_user(user=user, register=False, db=db)
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )


@router.post("/register", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, register=True, db=db)
    return user


@router.post("/role/grant", response_model=ShowUser)
def grant_role(user_id: int, role_name: str, db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        user = update_role_repo(user_id=user_id, role_name=role_name, db=db)
        return user
    if role_current.name == "MANAGER":
        if role_name == "ADMIN" or role_name == "MANAGER":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied.")
        user = update_role_repo(user_id=user_id, role_name=role_name, db=db)
        return user
    if role_current.name == "LEVEL1":
        if role_name == "ADMIN" or role_name == "MANAGER" or role_name == "LEVEL1":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied.", )
        user = update_role_repo(user_id=user_id, role_name=role_name, db=db)
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.")


@router.post("/role/revoke", response_model=ShowUser)
def grant_role(user_id: int, role_name: str, db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        user = update_role_repo(user_id=user_id, role_name=role_name, db=db)
        return user
    if role_current.name == "MANAGER":
        if role_name == "ADMIN" or role_name == "MANAGER":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied.")
        user = update_role_repo(user_id=user_id, role_name=role_name, db=db)
        return user
    if role_current.name == "LEVEL1":
        if role_name == "ADMIN" or role_name == "MANAGER" or role_name == "LEVEL1":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied.", )
        user = update_role_repo(user_id=user_id, role_name=role_name, db=db)
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.")
@router.post("/change-password", response_model=ShowUser)
def change_password(password: str, db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user_from_token)):
    return change_password_repo(current_user.id, password, db)
