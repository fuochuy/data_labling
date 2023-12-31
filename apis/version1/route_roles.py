from fastapi import status

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.roles import create_new_role, update_role_by_id, delete_role_by_id, list_role, get_role_by_name
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends

from schemas.roles import RoleBase
from sqlalchemy.orm import Session

router = APIRouter()


# @router.post("/", response_model=RoleBase)
# def create_role(role: RoleBase, db: Session = Depends(get_db),
#                 current_user: User = Depends(get_current_user_from_token)):
#     role_current = get_role_by_name(current_user.role, db)
#     if role_current.name == "ADMIN":
#         role = create_new_role(role=role, db=db)
#         return role
#     raise HTTPException(
#         status_code=status.HTTP_403_FORBIDDEN,
#         detail="Permission denied.",
#     )
@router.post("/")
def create_role(role: RoleBase, db: Session = Depends(get_db)):
    role = create_new_role(role=role, db=db)
    return role


# @router.put("/")
# def update_role(id: int, role: RoleBase, db: Session = Depends(get_db),
#                 current_user: User = Depends(get_current_user_from_token)):
#     role_current = get_role_by_name(current_user.role, db)
#     if role_current.name == "ADMIN":
#         return update_role_by_id(id, role=role, db=db)
#     raise HTTPException(
#         status_code=status.HTTP_403_FORBIDDEN,
#         detail="Permission denied.",
#     )
@router.put("/")
def update_role(id: int, role: RoleBase, db: Session = Depends(get_db)):
    return update_role_by_id(id, role=role, db=db)


@router.delete("/")
def delete_role(id: int, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        return delete_role_by_id(id, db=db)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )


@router.get("/")
def list(db: Session = Depends(get_db)):
    return list_role(db=db)
