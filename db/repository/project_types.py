from sqlalchemy.orm import Session

from db.models.project_types import ProjectType
from schemas.project_types import ProjectTypeBase


def create_new_type(type: ProjectTypeBase, db: Session):
    type_object = ProjectType(**type.dict())
    db.add(type_object)
    db.commit()
    db.refresh(type_object)
    return type


def list_type(db: Session):
    types = db.query(ProjectType).all()
    return types


def update_type_by_id(id: int, type: ProjectTypeBase, db: Session):
    existing_type = db.query(ProjectType).filter(ProjectType.id == id)
    if not existing_type.first():
        return 0
    type.__dict__.update(
        id=id
    )
    existing_type.update(type.__dict__)
    db.commit()
    return 1


def delete_type_by_id(id: int, db: Session):
    existing_type = db.query(ProjectType).filter(ProjectType.id == id)
    if not existing_type.first():
        return 0
    existing_type.delete(synchronize_session=False)
    db.commit()
    return 1


def get_type_by_name(name: str, db: Session):
    return db.query(ProjectType).filter(ProjectType.name == name).first()
