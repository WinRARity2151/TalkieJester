from .message_utils import send_typing_action, generate_response
from utils.options import bot

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    chat_id = message.chat.id
    try:
        send_typing_action(chat_id)
        bot.send_message(chat_id, generate_response(user_message))
    except Exception as e:
        print(e)
