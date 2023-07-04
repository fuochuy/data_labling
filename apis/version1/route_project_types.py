from fastapi import status

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.roles import get_role_by_name
from db.repository.project_types import create_new_type, update_type_by_id, delete_type_by_id, list_type, get_type_by_name
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends

from schemas.project_types import ProjectTypeBase
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ProjectTypeBase)
def create_type(type: ProjectTypeBase, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        type = create_new_type(type=type, db=db)
        return type
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )


@router.put("/")
def update_type(id: int, type: ProjectTypeBase, db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        return update_type_by_id(id, type=type, db=db)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )
    


@router.delete("/")
def delete_type(id: int, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        return delete_type_by_id(id, db=db)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )


@router.get("/")
def list(db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN":
        return list_type(db=db)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )
