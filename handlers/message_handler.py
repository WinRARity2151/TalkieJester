from .message_utils import send_typing_action, generate_response, process_voice_message
from utils.initializer import bot

def try_except_wrapper(func):
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapped

@bot.message_handler(content_types=['text'])
@try_except_wrapper
def handle_text_message(message):
    user_message = message.text
    chat_id = message.chat.id

    send_typing_action(chat_id)

    response = generate_response(user_message)
    bot.send_message(chat_id, response)

@bot.message_handler(content_types=['voice'])
@try_except_wrapper
def handle_voice_message(message):
    chat_id = message.chat.id
    send_typing_action(chat_id)

    voice_data = bot.download_file(bot.get_file(message.voice.file_id).file_path)
    recognized_text = process_voice_message(voice_data)
    response = generate_response(recognized_text)
    bot.send_message(chat_id, response)
