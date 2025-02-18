from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from sqlalchemy.ext.asyncio import create_async_engine

from .settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def init_models():
    async with engine.begin() as conn:
        # Виконуємо створення всіх таблиць у асинхронному режимі
        await conn.run_sync(Base.metadata.create_all)
