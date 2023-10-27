import os
import re
from typing import Pattern

from dotenv import load_dotenv

print(os.listdir())

if not load_dotenv(".env"):
    raise Exception("No envs are set")

TOKEN: str = os.environ["BOT_TOKEN"]

REGEXP_NSECONDS: Pattern[str] = re.compile(r"(\d+)\s+?seconds?")
# TODO: timex parser
# telegram trims messages
