from pydantic import BaseModel


# shared properties
class ProjectTypeBase(BaseModel):
    name: str
    description: str
