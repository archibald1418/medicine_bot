import pytest
from typing import Generator, Iterable
from . import TestingSessionFactory, engine
from sqlalchemy.orm import Session
from sqlalchemy.engine import Connection
from sqlalchemy import MetaData, Table
from app.models import BaseModel, User, Recipe, Medicine
from faker import Faker

from .utils.utils import truncate_all
# import sqlite3


@pytest.fixture(scope="function")  # this fixture wraps every test function
def db() -> Iterable[Session]:
    _db: Session = TestingSessionFactory()
    try:
        yield _db
    # session.commit()
    finally:
        _db.close()  # close regardless of exceptions


@pytest.fixture(scope="session", autouse=True) # works during the whole testing session and is used by every test by default
def setup_teardown_db() -> Iterable[None]:
    
    meta: MetaData = BaseModel.metadata
    
    def setup() -> None:
        with engine.connect() as conn:
            meta.drop_all(bind=conn, checkfirst=True)
            meta.create_all(bind=conn, checkfirst=True)
            truncate_all(conn, meta)
            conn.commit()

    def teardown() -> None:
        with engine.connect() as conn:
            # meta.drop_all(bind=conn)
            conn.commit()

    setup()
    yield
    teardown()


@pytest.fixture(scope="function")
def faker_obj() -> Iterable[Faker]:
    Faker.seed(42)
    yield Faker()

