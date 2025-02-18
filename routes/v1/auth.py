from sys import prefix
from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.post("/login")
async def login(): pass

@router.post("/refresh")
async def refresh(): pass

@router.delete("/logout")
async def logout(): pass
