from fastapi import status
from apis.version1.route_login import get_current_user_from_token

from db.models.users import User
from db.repository.projects import create_new_project, update_project_by_id, list_project, delete_project_by_id
from db.repository.roles import get_role_by_name
from db.session import get_db
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from schemas.projects import ProjectCreate, ShowProject, ProjectUpdate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowProject)
def create_project(project: ProjectCreate, db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user_from_token)   ):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN" or role_current.name == "MANAGER":
        project = create_new_project(project=project, username=current_user.username, db=db)
        return project
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )

@router.put("/")
def update_project(id: int, project: ProjectUpdate, db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN" or role_current.name == "MANAGER":
        return update_project_by_id(id, username=current_user.username, project=project, db=db)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )

@router.get("/")
def list(db: Session = Depends(get_db)):
    return list_project(db=db)

@router.delete("/")
def delete_type(id: int, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user_from_token)):
    role_current = get_role_by_name(current_user.role, db)
    if role_current.name == "ADMIN" or role_current.name == "MANAGER":
        return delete_project_by_id(id, db=db)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied.",
    )