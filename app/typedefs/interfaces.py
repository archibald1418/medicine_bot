from typing import Protocol, Optional, Generic, TypeVar
from sqlalchemy.orm import sessionmaker, DeclarativeBase


_Model = TypeVar("_Model", bound=DeclarativeBase, covariant=True)


class ILogger(Protocol):
    def log(self, msg: Optional[str]) -> None: ...


class ICrudService(Protocol, Generic[_Model]):

    sessionFactory: sessionmaker

    @staticmethod
    def get(*args, **kwargs) -> _Model: ...
    
    @staticmethod
    def create(*args, **kwargs) -> _Model: ...
    
    @staticmethod
    def update(*args, **kwargs) -> _Model: ...
    
    @staticmethod
    def delete(*args, **kwargs) -> None: ...
