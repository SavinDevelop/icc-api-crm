from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from typing import Optional, List

from models.user import User 

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: int) -> Optional[User]:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_by_email(self, email: str) -> Optional[User]:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> List[User]:
        query = select(User)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update(self, user: User) -> User:
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def deactive(self, user: User) -> User:
        user.active = False
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete(self, user: User):
        await self.session.delete(user)
        await self.session.commit()

    async def get_with_worker(self, user_id: int) -> Optional[User]:
        query = select(User).options(joinedload(User.worker)).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalars().first()