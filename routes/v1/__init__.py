from fastapi import APIRouter

from . import user

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(user.router, tags=["user"])
