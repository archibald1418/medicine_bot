from typing import Literal, TypeAlias, Callable, Optional, Protocol
from telebot.types import Message
import logging


FileMode: TypeAlias = Literal["r", "w", "a", "x"]

LogLevel: TypeAlias = int | str

MsgFilter: TypeAlias = Callable[[Message], bool]

class ILogger(Protocol):
    def log(self, msg: Optional[str]) -> None: ...