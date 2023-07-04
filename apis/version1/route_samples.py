from db.repository.sample import create_sample, list_by_project_id, update_label, delete_by_id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.samples import CreateSample, ShowSample
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/sample")
def create(sample: CreateSample, db: Session = Depends(get_db)):
    sample = create_sample(sample=sample, db=db)
    return sample


@router.get("/")
def list(project_id: int, status: bool, db: Session = Depends(get_db)):
    sample = list_by_project_id(project_id, status, db)
    return sample


@router.put("/lable")
def label(id: str, lable: str, db: Session = Depends(get_db)):
    sample = update_label(id, lable, db)
    return sample


@router.delete("/")
def label(id: str, db: Session = Depends(get_db)):
    return delete_by_id(id, db)
