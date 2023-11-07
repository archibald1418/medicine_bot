import telebot
from .config import BOT_TOKEN
from .log.logger import Logger
from .config import DBURL
import logging

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker

# Globals
bot = telebot.TeleBot(BOT_TOKEN, threaded=True)
logger = Logger()
engine: Engine = create_engine(DBURL)

SessionFactory: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
