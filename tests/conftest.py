import pytest
from typing import Generator
from . import TestingSessionFactory, engine
from sqlalchemy.orm import Session
from app.models import BaseModel, User, Recipe, Medicine
from faker import Faker


@pytest.fixture(scope="function")  # this fixture wraps every test function
def db() -> Generator[Session, None, None]:
    _db: Session = TestingSessionFactory()
    try:
        yield _db
    # session.commit()
    finally:
        _db.close()  # close regardless of exceptions


@pytest.fixture(scope="session", autouse=True) # works during the whole testing session and is used by every test by default
def setup_teardown_db():
    def setup() -> None:
        with engine.connect() as conn:
            BaseModel.metadata.create_all(bind=conn)
            conn.commit()

    def teardown() -> None:
        with engine.connect() as conn:
            BaseModel.metadata.drop_all(bind=conn)
            conn.commit()

    setup()
    yield
    teardown()


@pytest.fixture(scope="function")
def faker_obj():
    faker = Faker()
    faker.seed(42)
    
    yield faker

