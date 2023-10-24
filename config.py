import os
import re
from typing import Pattern
from telebot import TeleBot

from dotenv import load_dotenv

load_dotenv('.env')

TOKEN: str = os.environ["BOT_TOKEN"]

REGEXP_NSECONDS: Pattern[str] = re.compile(r"(\d+)\s+?seconds?")
# TODO: timex parser
# telegram trims messages
