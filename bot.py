
from dotenv import load_dotenv
import os
import telebot
from telebot.types import Message
from typing import Callable, TypeAlias

load_dotenv('.env')
# print(os.getenv("BOT_TOKEN"))

MsgFilter: TypeAlias = Callable[[Message], bool]

AnyMessage: MsgFilter = lambda msg: True
TextMessage: MsgFilter = lambda msg: msg.content_type == 'text'


TOKEN: str = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_hello(msg: Message):
    bot.reply_to(msg, "Howdy how are you doing?")



@bot.message_handler(func=TextMessage)
def echo_all(msg: Message):
    bot.reply_to(msg, msg.text)


if __name__ == '__main__':
    bot.infinity_polling()