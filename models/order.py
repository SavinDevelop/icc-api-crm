from __future__ import annotations

from datetime import datetime

from sqlalchemy import Integer, Text, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from core.database import Base


class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)



    date_created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    date_updated: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc))



class Comment(Base):
    __tablename__ = "order_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    

class Work(Base):
    __tablename__ = "order_work"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Status(Base):
    __tablename__ = "order_status"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
