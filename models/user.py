from __future__ import annotations
from typing import Optional

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Boolean, Text, DateTime

from core.database import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    full_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String(255))

    active: Mapped[bool] = mapped_column(Boolean, default=True)
    admin: Mapped[bool] = mapped_column(Boolean, default=False)

    worker: Mapped[Optional[Worker]] = relationship(
        "Worker", back_populates="user", uselist=False
    )

    date_created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    date_updated: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc))


class Worker(Base):
    __tablename__ = "worker"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    departament: Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), unique=True)
    user: Mapped[User] = relationship("User", back_populates="worker")

    job_id: Mapped[int] = mapped_column(ForeignKey("job.id"))
    job: Mapped[Job] = relationship("Job", back_populates="workers")


class Job(Base):
    __tablename__ = "job"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(255))

    workers: Mapped[list[Worker]] = relationship("Worker", back_populates="job")
