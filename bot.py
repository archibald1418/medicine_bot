
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


TOKEN: str  = os.environ["BOT_TOKEN"]
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_hello(msg: Message):
    bot.reply_to(msg, "Howdy how are you doing?")



@bot.message_handler(func=TextMessage)
def echo_all(msg: Message):
    bot.reply_to(msg, msg.text)


if __name__ == '__main__':
    bot.infinity_polling()