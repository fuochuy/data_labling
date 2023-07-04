from pydantic import BaseModel
from pydantic.schema import datetime


class ShowSample(BaseModel):
    id: int
    project_id: int
    sample: str
    label: str
    status: bool
    created_user: int
    update_user: int


class CreateSample(BaseModel):
    project_id: int
    sample: str
    label: str
    user_id: int


class UpdateSample(BaseModel):
    id: int
    project_id: int
    label: str
    user_id: int
