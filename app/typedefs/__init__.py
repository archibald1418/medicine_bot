from typing import Literal, TypeAlias, Callable, Optional, Protocol, Generic, TypeVar
from telebot.types import Message
import logging

from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


FileMode: TypeAlias = Literal["r", "w", "a", "x"]

LogLevel: TypeAlias = int | str

MsgFilter: TypeAlias = Callable[[Message], bool]


