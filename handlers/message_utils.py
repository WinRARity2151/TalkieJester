from utils.options import bot
import g4f

def send_typing_action(chat_id):
    bot.send_chat_action(chat_id, 'typing')

def generate_response(user_message):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
    )
    return response
