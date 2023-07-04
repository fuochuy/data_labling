from pydantic import BaseModel

class ProjectCreate(BaseModel):
    projectName: str
    projectType: str
    description: str
    status: str


class ShowProject(BaseModel):
    projectId: int
    projectName: str
    projectType: str
    description: str
    status: str
    created_user: str

    class Config:  # to convert non dict obj to json
        orm_mode = True


class ProjectUpdate(BaseModel):
    projectName: str
    description: str
    status: str
    updated_user: str
