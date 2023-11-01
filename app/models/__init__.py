import uuid

from typing import List, Optional
import datetime
from sqlalchemy import ForeignKey, String, Integer, DateTime, DATETIME, Uuid
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)

class Base(DeclarativeBase): ...

class Medicine(Base):
    __tablename__ = "medicine"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    recipes: Mapped[List["Recipe"]] = relationship(back_populates="medicine") 
    users: Mapped[List["User"]] = relationship(back_populates="medicines")

    def __repr__(self) -> str:
        return f"Medicine(id={self.id!r}, name={self.name!r})"

class Recipe(Base):

    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    fk_medicine_id: Mapped[Integer] = ForeignKey("medicine.id", nullable=False)
    sttm: Mapped[datetime.datetime] = mapped_column()
    ettm: Mapped[datetime.datetime] = mapped_column()
    # ... TODO: more parsing info for recipe

    user: Mapped["User"] = relationship(back_populates="recipes") # one user follows many recipes
    medicine: Mapped[Medicine] = relationship(back_populates="recipes") # one medicine appears in many recipes
    # recipes don't pile up as fast as medicines or users (for now)


class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4, unique=True, autoincrement=False)
    fk_recipe_id: Mapped[int] = ForeignKey("recipe.id", nullable=True)

    medicines: Mapped[List[Medicine]] = relationship(back_populates="users") # one user takes many medicines
    recipes: Mapped[Recipe] = relationship(back_populates="user")
