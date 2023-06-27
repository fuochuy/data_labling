from pydantic import BaseModel


# shared properties
class RoleBase(BaseModel):
    name: str
    description: str
