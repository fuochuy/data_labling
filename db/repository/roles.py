from sqlalchemy.orm import Session

from db.models.roles import Role
from schemas.roles import RoleBase


def create_new_role(role: RoleBase, db: Session):
    role_object = Role(**role.dict())
    db.add(role_object)
    db.commit()
    db.refresh(role_object)
    return role


def list_role(db: Session):
    roles = db.query(Role).all()
    return roles


def update_role_by_id(id: int, role: RoleBase, db: Session):
    existing_role = db.query(Role).filter(Role.id == id)
    if not existing_role.first():
        return 0
    role.__dict__.update(
        id=id
    )
    existing_role.update(role.__dict__)
    db.commit()
    return 1


def delete_role_by_id(id: int, db: Session):
    existing_role = db.query(Role).filter(Role.id == id)
    if not existing_role.first():
        return 0
    existing_role.delete(synchronize_session=False)
    db.commit()
    return 1


def get_role_by_name(name: str, db: Session):
    return db.query(Role).filter(Role.name == name).first()
