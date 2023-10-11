from utils.initializer import bot
from handlers.message_handler import handle_text_message, handle_voice_message

if __name__ == '__main__':
    bot.polling(none_stop=True)
