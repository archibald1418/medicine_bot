# import sqlite3
from sqlalchemy import Engine, Connection, Result, TextClause
from sqlalchemy import (
    create_engine,
    text
)
import logging
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL


# TODO for a server part
username: str
password: str
host: str
port: int

db: str = "sqlite"
dbapi: str = "pysqlite"
filename: str = ":memory:"  # in-memory database

dburl: URL = f"{db}+{dbapi}:///{filename}"
# postgresql+pg8000://dbuser:kx%40jj5%2Fg@pghost10/appdb

engine: Engine = create_engine(dburl)


def conn():
    conn: Connection

    # 'with engine.begin()' will automatically commit everything in the block
    with engine.connect() as conn:
        result: Result = conn.execute(text("SELECT 'hello from the other side'"))
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
        )
        conn.commit()
        # print(result.all())

    # rows
    with engine.connect() as conn:
        result: Result = conn.execute(text("SELECT x, y FROM some_table"))
        for row in result:
            print(f"x: {row.x}  y: {row.y}")
    
    # parameters
    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2})
        for row in result:
            print(f"x: {row.x}  y: {row.y}")
    
    # multiple params (this is a certified swine)
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
        )
        conn.commit()

    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM some_table"))
        print("fetched:", *result.all(), sep='\n')


def session():
    session: Session = Session(engine)

    stmt: TextClause = text("SELECT * FROM some_table WHERE y > :y ORDER BY x, y")
    
    with session:
        result: Result = session.execute(stmt, {"y": 6})
        for row in result.mappings():
            for k, v in row.items():
                print(k, v, sep=':')
    
    with Session(engine) as session:
        result = session.execute(
            text("UPDATE some_table SET y=:y WHERE x=:x"),
            [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
        )
        session.commit()
        session.add



def main():
    conn()
    session()
    


if __name__ == '__main__':
    logging.basicConfig(filename="db.log", filemode='w')
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

    main()

"""
NOTE: for using a python logger instead of echo=True
    import logging
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
"""
