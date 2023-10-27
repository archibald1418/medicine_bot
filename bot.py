import re
import time
import logging
from decorators import call_counter

from typing import Optional
from extra_types import FileMode, LogLevel, IsTextMessage, BlockHandler, ILogger

import telebot
from telebot.types import Message

from config import TOKEN, REGEXP_NSECONDS


class Logger(ILogger):
    def __init__(
        self,
        filename: str = "timerbot.log",
        encoding: str = "utf8",
        filemode: FileMode = "w",
        level: Optional[LogLevel] = logging.DEBUG,
    ):
        logging.basicConfig(
            filename=filename, filemode=filemode, level=level, encoding=encoding
        )

    def log(self, msg: Optional[str] = None):
        logging.info(f"[{time.ctime(time.time())}]: {msg or 'OK'}")


# Globals
bot = telebot.TeleBot(TOKEN, threaded=True)
logger = Logger()


@bot.message_handler(func=BlockHandler)
@call_counter
def echo_all(self, msg: Message):
    assert msg.text
    self.bot.reply_to(msg, msg.text)


@bot.message_handler(func=IsTextMessage)
@call_counter
def timex(msg: Message):
    if msg.text:
        logger.log(f"Request {timex.calls}: '{msg.text}'")

        if match := re.match(REGEXP_NSECONDS, msg.text):
            seconds = int(match.group(1))

            """Sleep here"""
            time.sleep(seconds)
            logger.log(f"Request {timex.calls} waited {seconds} seconds")

            bot.reply_to(msg, f"{seconds} seconds passed!")
        else:
            bot.reply_to(msg, "Command is invalid: please write number of seconds")


def run():
    bot.infinity_polling()


def main():
    logger.log("Run ..")
    run()


if __name__ == "__main__":
    main()
