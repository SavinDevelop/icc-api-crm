from sys import prefix
from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.post("/login")
async def login(): pass

@router.refresh("/refresh")
async def refresh(): pass

@router.post("/logout")
async def logout(): pass
