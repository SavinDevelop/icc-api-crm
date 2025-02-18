from core.database import init_models

from fastapi import FastAPI

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()  
    yield 
    
app = FastAPI(lifespan=lifespan)

