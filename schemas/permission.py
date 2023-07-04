from pydantic import BaseModel


class PermissionCreate(BaseModel):
    endpoint: str
    action: str
    authenticationEnable: bool
    authorizationEnable: bool
    methods: str
    label: str


class PermissionUpdate(BaseModel):
    id: int
    endpoint: str
    action: str
    authenticationEnable: bool
    authorizationEnable: bool
    methods: str
    label: str
