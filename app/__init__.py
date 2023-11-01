import telebot
from .config import BOT_TOKEN
from .log.logger import Logger
from .config import DBURL
import logging

from sqlalchemy import Engine, create_engine

# Globals
bot = telebot.TeleBot(BOT_TOKEN, threaded=True)
logger = Logger()
db_engine: Engine = create_engine(DBURL)

