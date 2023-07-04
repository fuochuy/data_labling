from apis.version1 import route_login, route_roles, route_project_types, route_projects, route_samples
from apis.version1 import route_users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_roles.router, prefix="/roles", tags=["roles"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_project_types.router, prefix="/types", tags=["types"])
api_router.include_router(route_projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(route_samples.router, prefix="/samples", tags=["samples"])
