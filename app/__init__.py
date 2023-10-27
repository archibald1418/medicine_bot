import telebot
from .config import TOKEN
from .log.logger import Logger

# Globals
bot = telebot.TeleBot(TOKEN, threaded=True)
logger = Logger()