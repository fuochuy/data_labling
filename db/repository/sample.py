import datetime
from sqlalchemy.orm import Session
from db.models.sample import Sample
from schemas.samples import CreateSample, UpdateSample


def create_sample(sample: CreateSample, db: Session):
    sample = Sample(
        project_id=sample.project_id,
        sample=sample.sample,
        label=sample.label,
        status=False,
        created_user=sample.user_id,
        updated_user=sample.user_id,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    db.add(sample)
    db.commit()
    db.refresh(sample)
    return sample


def update_sample(sample: UpdateSample, db: Session):
    existing_sample = db.query(Sample).filter(Sample.id == sample.id and Sample.project_id == sample.project_id).first()
    if not existing_sample:
        return None
    existing_sample.label = sample.label
    existing_sample.updated_user = sample.user_id
    existing_sample.updated_at = datetime.datetime.now()
    if sample.label is not None:
        existing_sample.status = True
    else:
        existing_sample.status = False
    existing_sample.update()
    return existing_sample


def list_by_project_id(project_id: int, status: bool, db: Session):
    if status is not None:
        samples = db.query(Sample).filter(Sample.project_id == project_id and Sample.status == status).all()
        return samples
    else:
        samples = db.query(Sample).filter(Sample.project_id == project_id).all()
        return samples

def get_by_id(id: int, db: Session):
    samples = db.query(Sample).filter(Sample.id == id).all()
    return samples


def delete_by_id(id: int, db: Session):
    existing_sample = db.query(Sample).filter(Sample.id == id)
    if not existing_sample.first():
        return 0
    existing_sample.delete(synchronize_session=False)
    db.commit()
    return 1
