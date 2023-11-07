from __future__ import annotations

import uuid
import datetime
from typing import List, TypeAlias

from sqlalchemy import Column, ForeignKey, String, Enum as AlchemyEnum, DateTime, Table
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

from ..typedefs.enums import TimeOfMedicine


UserId: TypeAlias = uuid.UUID


class BaseModel(DeclarativeBase):
    ...


class Medicine(BaseModel):
    __tablename__ = "medicine"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    recipes: Mapped[List[Recipe]] = relationship(back_populates="medicine")
    # users: Mapped[List["User"]] = relationship(back_populates="medicines")

    def __repr__(self) -> str:
        return f"Medicine(id={self.id!r}, name={self.name!r})"


class Recipe(BaseModel):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    fk_medicine_id: Mapped[int] = mapped_column(
        ForeignKey(
            "medicine.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    medicine: Mapped[Medicine] = relationship(back_populates="recipes")

    fk_user_id: Mapped[UserId] = mapped_column(
        ForeignKey(
            "user.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    user: Mapped[User] = relationship(back_populates="recipes")
    # NOTE: mapped attrs are lazy-loaded (=memoized with active session instance!)

    how_to_take: Mapped[TimeOfMedicine] = mapped_column(
        AlchemyEnum(TimeOfMedicine),
        default=TimeOfMedicine.NOTSTATED
    )
    npills: Mapped[int] = mapped_column(default=0)
    ndays: Mapped[int] = mapped_column(default=0)
    sttm: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    ettm: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    # ... INPROGRESS: more parsing info for recipe

    def __repr__(self) -> str:
        return f"Recipe(id={self.id}, medicine_id={self.fk_medicine_id})"


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[UserId] = mapped_column(
        primary_key=True, default=uuid.uuid4, unique=True, autoincrement=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    recipes: Mapped[List[Recipe]] = relationship(
        back_populates="user", cascade="all, delete")
    # medicines: List[Mapped[Medicine]] = relationship(back_populates="users")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name or '...'})"


# TODO: many-to-many:
# user_takes_medicine = Table(
#     "takes",
#     Base.metadata,
#     Column("fk_user_id", ForeignKey("user.id", primary_key=True)),
#     Column("fk_medicine_id", ForeignKey("medicine.id", primary_key=True))
# )
