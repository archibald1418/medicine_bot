
import os
import re
import sched
import time
import logging

from typing import Callable, TypeAlias, Optional

import telebot
from telebot.types import Message

from config import TOKEN, REGEXP_NSECONDS

MsgFilter: TypeAlias = Callable[[Message], bool]

any_message: MsgFilter = lambda msg: True
text_message: MsgFilter = lambda msg: msg.content_type == 'text'
block_handler: MsgFilter = lambda msg: False


class Logger:

    def __init__ (self):
        self.logger = logging.basicConfig(filename='timerbot.log', encoding='utf8', filemode='w', level=logging.DEBUG)
        # self.logger = telebot.logger.setLevel(logging.DEBUG)

    def log(self, msg: Optional[str] = None):
        logging.info(f"[{time.ctime(time.time())}]: {msg or 'OK'}")



# Globals
bot = telebot.TeleBot(TOKEN, threaded=True)
logger = Logger()
requests = 0


# Decorator for updating number of requests
def upd_count(handler):
    
    def inner(*args, **kwargs):
        global requests
        requests += 1
        handler(*args, **kwargs)
    
    return inner


@bot.message_handler(commands=['start', 'hello'])
@upd_count
def send_hello(msg: Message):
    bot.reply_to(msg, "Howdy how are you doing?")

@bot.message_handler(func=block_handler)
@upd_count
def echo_all(self, msg: Message):
    assert(msg.text)
    self.bot.reply_to(msg, msg.text)



@bot.message_handler(func=text_message)
@upd_count
def timex(msg: Message):
    if msg.text:
        logger.log(f"Request {requests}: '{msg.text}'")

        if (match := re.match(REGEXP_NSECONDS, msg.text)):
            seconds = int(match.group(1))

            '''Sleep here'''
            time.sleep(seconds)
            logger.log(f"Request {requests} waited {seconds} seconds")
            
            bot.reply_to(msg, f"{seconds} seconds passed!")
        else:
            bot.reply_to(msg, "Command is invalid: please write number of seconds")


def run():
    bot.infinity_polling()


def main():
    logger.log("Run ..")
    run()


if __name__ == '__main__':
    main()