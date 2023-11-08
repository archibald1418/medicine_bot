import logging
import os

from dotenv import load_dotenv
from sqlalchemy.engine import Engine, create_engine, URL, make_url
from sqlalchemy.pool import StaticPool  # re-use same connection for all requests
from sqlalchemy.orm import sessionmaker, Session

load_dotenv(".env.test")

DB: str = os.environ['DB']
DBAPI: str = os.environ['DBAPI']
DBFILE: str = os.environ['DBFILE']

DBURL: URL = make_url(f"{DB}+{DBAPI}:///{DBFILE}")

engine: Engine = create_engine(
    DBURL,
    connect_args={
        "check_same_thread": False
    },
    poolclass=StaticPool,  # a shared connection
    # echo=True
)


TestingSessionFactory: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

logging.basicConfig(
    filename='app/log/sqlengine.log',
    filemode='w'
)
logging.getLogger("sqlalchemy.engine.Engine").setLevel(logging.INFO)
