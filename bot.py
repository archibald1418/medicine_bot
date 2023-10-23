
from dotenv import load_dotenv
import os
import telebot
from telebot.types import Message
from telebot import TeleBot
from typing import Callable, TypeAlias, Pattern
import re

load_dotenv('.env')
# print(os.getenv("BOT_TOKEN"))

MsgFilter: TypeAlias = Callable[[Message], bool]

any_message: MsgFilter = lambda msg: True
text_message: MsgFilter = lambda msg: msg.content_type == 'text'
block_handler: MsgFilter = lambda msg: False


TOKEN: str  = os.environ["BOT_TOKEN"]
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_hello(msg: Message):
    bot.reply_to(msg, "Howdy how are you doing?")



@bot.message_handler(func=block_handler)
def echo_all(msg: Message):
    assert(msg.text)
    bot.reply_to(msg, msg.text)


REGEXP_NSECONDS: Pattern[str] = re.compile(r"^\s*?(\d+)\s+?seconds?")

@bot.message_handler(func=text_message)
def timex(msg: Message):
    if msg.text:
        print(repr(msg.text))
        if (match := re.match(REGEXP_NSECONDS, msg.text)):
            seconds = int(match.group(1))

            '''Sleep here'''
            
            bot.reply_to(msg, f"{seconds} seconds passed!")
        else:
            bot.reply_to(msg, "Command is invalid: please write number of seconds")


if __name__ == '__main__':
    bot.infinity_polling()