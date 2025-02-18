from __future__ import annotations

from datetime import datetime
from turtle import title

from sqlalchemy import Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from core.database import Base


class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)

    comments: Mapped[list["Comment"]] = relationship(back_populates="order")

    work_id: Mapped[int] = mapped_column(ForeignKey("order_work.id"))
    work: Mapped["Work"] = relationship(back_populates="orders")


    date_created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    date_updated: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc))


class Comment(Base):
    __tablename__ = "order_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text)

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    order: Mapped["Order"] = relationship(back_populates="comment")

    status_history: Mapped[list["OrderStatusHistory"]] = relationship(back_populates="order", cascade="all, delete-orphan")


    date_created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    

class Work(Base):
    __tablename__ = "order_work"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    orders: Mapped[list["Order"]] = relationship(back_populates="work")
    

class Status(Base):
    __tablename__ = "order_status"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    date_created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))


class OrderStatusHistory(Base):
    __tablename__ = "order_status_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("order_status.id"))
    changed_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))

    order: Mapped["Order"] = relationship(back_populates="status_history")
    status: Mapped["Status"] = relationship()