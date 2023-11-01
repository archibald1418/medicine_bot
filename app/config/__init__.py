import os
import re
from typing import Pattern
from sqlalchemy import URL

from dotenv import load_dotenv

print(os.listdir())

if not load_dotenv(".env"):
    raise Exception("No envs are set")

BOT_TOKEN: str = os.environ["BOT_TOKEN"]

REGEXP_NSECONDS: Pattern[str] = re.compile(r"(\d+)\s+?seconds?")
# telegram trims messages

# Database
username: str
password: str
host: str
port: int

DB: str = os.environ["DB"]
DBAPI: str = os.environ["DBAPI"]
DBFILE: str = os.environ["DBFILE"]  # in-memory database

DBURL: URL = f"{DB}+{DBAPI}:///{DBFILE}"
