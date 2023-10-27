import re
import time
from telebot.types import Message

from app.utils.decorators import call_counter

from app.typedefs.filters import IsTextMessage # 'types' is also a package from telegram
from app.config import REGEXP_NSECONDS

from app import logger, bot


# @bot.message_handler(func=BlockHandler)
# @call_counter
# def echo_all(self, msg: Message):
#     assert msg.text
#     self.bot.reply_to(msg, msg.text)


# TODO: bot-runner-class without filters when the UI is ready
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
