from typing import Literal, TypeAlias, Callable, Optional, Protocol
from telebot.types import Message
from enum import Enum
import logging


FileMode: TypeAlias = Literal["r", "w", "a", "x"]

LogLevel: TypeAlias = logging._Level

MsgFilter: TypeAlias = Callable[[Message], bool]

AnyMessage: MsgFilter = lambda msg: True
TextMessage: MsgFilter = lambda msg: msg.content_type == "text"
BlockHandler: MsgFilter = lambda msg: False

class ILogger(Protocol):
    def log(self, msg: Optional[str]): ...