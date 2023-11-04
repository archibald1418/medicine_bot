import uuid

from typing import List, Optional
import datetime
from sqlalchemy import ForeignKey, String, Enum as AlchemyEnum, DateTime
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)
from ..typedefs.enums import TimeOfMedicine


class Base(DeclarativeBase):
    ...


class Medicine(Base):
    __tablename__ = "medicine"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    recipes: Mapped[List["Recipe"]] = relationship(back_populates="medicine", cascade='all, delete')
    users: Mapped[List["User"]] = relationship(back_populates="medicines")

    def __repr__(self) -> str:
        return f"Medicine(id={self.id!r}, name={self.name!r})"


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    fk_medicine_id: Mapped[int] = ForeignKey("medicine.id", nullable=False)
    how_to_take: Mapped[TimeOfMedicine] = mapped_column(AlchemyEnum(TimeOfMedicine),
                                                        default=TimeOfMedicine.NOTSTATED)
    npills: Mapped[int] = mapped_column(default=0)
    ndays: Mapped[int] = mapped_column(default=0)
    sttm: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    ettm: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    # ... INPROGRESS: more parsing info for recipe

    user: Mapped["User"] = relationship(
        back_populates="recipes"
    )  # one user follows many recipes
    medicine: Mapped[Medicine] = relationship(
        back_populates="recipes"
    )  # one medicine appears in many recipes
    # recipes don't pile up as fast as medicines or users (for now)


class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, unique=True, autoincrement=False
    )
    fk_recipe_id: Mapped[int] = ForeignKey("recipe.id", nullable=True, ondelete="CASCADE")

    medicines: Mapped[List[Medicine]] = relationship(
        back_populates="users",
        cascade="all, delete"
    )  # one user takes many medicines
    recipes: Mapped[Recipe] = relationship(back_populates="user", cascade="all, delete")
