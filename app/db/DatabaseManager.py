from typing import ContextManager
from sqlalchemy import Engine, Connection
import types
from typing import Optional, Literal
import traceback
import logging



class DatabaseManager(ContextManager):
    
    def __init__(self, db_engine: Engine):
        self._db_engine: Engine = db_engine
        self.__conn: Connection | None = None
    
    def __enter__(self) -> Connection:
        if self.__conn is None or self.__conn.closed:
            self.__conn = self._db_engine.connect()
        return self.__conn
    
    def __exit__(self,
                 exc_type: Optional[type],
                 exc_value: Optional[Exception],
                 tb: Optional[types.TracebackType]
            ) -> None | Literal[True]:
        if exc_type:
            traceback.print_tb(tb)
            return True
        del self.conn
    
    @property
    def conn(self) -> Connection:
        return self.__conn

    @conn.deleter
    def conn(self) -> None:
        if self.__conn and not self.__conn.closed:
            self.__conn.close()
        self.__conn = None
    
    @property
    def db_engine(self) -> Engine:
        return self._db_engine
    
    @db_engine.setter
    def db_engine(self, other: Engine) -> None:
        self._db_engine = other
        del self.__conn
