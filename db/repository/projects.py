import datetime
from fastapi import HTTPException
from fastapi import status

from db.models.project_types import ProjectType
from db.models.projects import Project
from schemas.projects import ProjectCreate, ProjectUpdate
from sqlalchemy.orm import Session


def create_new_project(project: ProjectCreate, username: str, db: Session):
    type = db.query(ProjectType).filter(ProjectType.name == project.projectType).first()
    if type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found type with name is %s".format(project.projectType)
        )
    project = Project(
        projectName = project.projectName,
        projectType = type.name,
        created_user = username,
        created_date = datetime.datetime.utcnow,
        updated_user = username,
        updated_date = datetime.datetime.utcnow,
        description = project.description,
        status = project.status
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_project_by_created_user(created_user: str, db: Session):
    projects = db.query(Project).filter(projects.created_user == created_user)
    return projects


def list_project(db: Session):
    projects = db.query(Project).all()
    return projects


def update_project_by_id(id: int, username: str, project: ProjectUpdate, db: Session):
    existing_project = db.query(Project).filter(Project.projectId == id).first()
    if not existing_project:
        return 0
    if project.projectName is not None:
        existing_project.projectName = project.projectName
    if project.description is not None:
        existing_project.description = project.description
    if project.status is not None:
        existing_project.status = project.status
    if project.projectName is not None or project.description is not None or project.status is not None:
        existing_project.updated_user = username
        existing_project.updated_date = datetime.datetime.utcnow
    
    existing_project.update()
    db.commit()
    return 1

def delete_project_by_id(id: int, db: Session):
    existing_project = db.query(Project).filter(Project.projectId == id)
    if not existing_project.first():
        return 0
    existing_project.delete(synchronize_session=False)
    db.commit()
    return 1

