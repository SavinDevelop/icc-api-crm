from fastapi import APIRouter

router = APIRouter()

@router.get("/users", response_model=list[str])
async def get_list_users(): pass

@router.get("/user/{email}", response_model=str)
async def get_user_by_email(): pass

@router.post("/user")
async def crate_user(): pass

@router.put("/user", response_model=str)
async def update_user(): pass

@router.delete("/user")
async def delete_user(): pass
