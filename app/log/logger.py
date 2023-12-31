from ..typedefs import FileMode, LogLevel
from ..typedefs.interfaces import ILogger
from typing import Optional
import logging
import time


class Logger(ILogger):
    def __init__(
        self,
        filename: str = "app/log/bot.log",
        encoding: str = "utf8",
        filemode: FileMode = "w",
        level: Optional[LogLevel] = logging.INFO,
    ):
        logging.basicConfig(
            filename=filename, filemode=filemode, level=level, encoding=encoding
        )

    def log(self, msg: Optional[str] = None) -> None:
        logging.info(f"[{time.ctime(time.time())}]: {msg or 'OK'}")
