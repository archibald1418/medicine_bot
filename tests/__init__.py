from app.db.DatabaseManager import DatabaseManager
from app import db_engine
import logging

import pytest


db_ctx: DatabaseManager = DatabaseManager(db_engine)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)
# with pytest doesn't allow writing to file with -s and -p no:logging