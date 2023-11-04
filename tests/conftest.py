import pytest
from typing import Generator
from . import TestingSessionFactory
from sqlalchemy.orm import Session

@pytest.fixture
def db() -> Generator[Session, None, None]:
    _db: Session = TestingSessionFactory()
    try:
        yield _db
    # session.commit()
    finally:
        _db.close() # close regardless of exceptions
