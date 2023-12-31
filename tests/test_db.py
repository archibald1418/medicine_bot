from sqlalchemy import Connection, Result, TextClause, MetaData
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound
import pytest
from app.models import User, Medicine, Recipe

from app.models import cruds


@pytest.mark.skip(reason="Inactive")
def test_insert_db(db: Session) -> None:
    with db:
        # try:
        user: User | None = cruds.user.add_user("John", db)
        assert user and user.id
        assert cruds.user.get_user_by_id(user.id, db) == user
        assert cruds.user.get_user_by_name("John", db) == user
        # except MultipleResultsFound:




def test_fill_db(db: Session, faker_obj) -> None:
    with db:
        nrows = 10
        for i in range(nrows):
            name: str = faker_obj.name()
            medicine: str = faker_obj.safe_color_name()

            cruds.user.add_user(name, db)
            cruds.medicine.add_medicine(medicine, db)
        
        assert db.execute(
            text("SELECT COUNT(*) from user")
        ).scalar_one() == nrows
        
        assert db.execute(
            text("SELECT COUNT(*) from medicine")
        ).scalar_one() == nrows


@pytest.mark.skip(reason='this is a sandbox test')
def test_db(db: Session) -> None:
    # 'with db_engine.begin()' will automatically commit everything in the block
    with db as conn:
        result: Result = conn.execute(text("SELECT 'hello from the other side'"))
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
        )
        conn.commit()
        print(result.all())

    # rows
    with db as conn:
        result: Result = conn.execute(text("SELECT x, y FROM some_table"))
        for row in result:
            print(f"x: {row.x}  y: {row.y}")

    # parameters
    with db as conn:
        result = conn.execute(
            text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2}
        )
        for row in result:
            print(f"x: {row.x}  y: {row.y}")

    # multiple params (this is a certified swine)
    with db as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
        )
        conn.commit()

    with db as conn:
        result = conn.execute(text("SELECT * FROM some_table"))
        print("fetched:", *result.all(), sep="\n")


# def setup() -> None:
#     # with db.connection() as conn:
#     models.Base.metadata.create_all(bind=engine)
#         # db.commit()

# def teardown() -> None:
#     # with db.connection() as conn:
#     models.Base.metadata.drop_all(bind=engine)
#         # db.commit()

# def test_db_session():
#     session: Session = Session(db_ctx.db_engine)

#     stmt: TextClause = text("SELECT * FROM some_table WHERE y > :y ORDER BY x, y")

#     with session:
#         result: Result = session.execute(stmt, {"y": 6})
#         for row in result.mappings():
#             for k, v in row.items():
#                 print(k, v, sep=':')

#     with Session(db_ctx.db_engine) as session:
#         result = session.execute(
#             text("UPDATE some_table SET y=:y WHERE x=:x"),
#             [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
#         )
#         session.commit()
#         # session.add


if __name__ == "__main__":
    print("I AM NOT A MODULE")

"""
NOTE: for using a python logger instead of echo=True
    import logging
    logging.basicConfig()
    logging.getLogger("sqlalchemy.db_engine").setLevel(logging.INFO)
"""
