from utils.options import bot
import telebot
from handlers.message_handler import handle_message

if __name__ == '__main__':
    bot.polling(none_stop=True)
