from db.repository.sample import create_sample, list_by_project_id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.samples import CreateSample, ShowSample
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowSample)
def create(sample: CreateSample, db: Session = Depends(get_db)):
    sample = create_sample(sample=sample, db=db)
    return sample


@router.get("/", response_model=list[ShowSample])
def list(project_id: int, status: bool, db: Session = Depends(get_db)):
    sample = list_by_project_id(project_id, status, db)
    return sample
