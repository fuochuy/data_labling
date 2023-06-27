from pydantic import BaseModel
from pydantic import EmailStr


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    fullname: str
    role: str


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    fullname: str
    is_active: bool
    role: str

    class Config:  # to convert non dict obj to json
        orm_mode = True


class UserUpdate(BaseModel):
    fullname: str
    email: EmailStr
    password: str
    role: str
