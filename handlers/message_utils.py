from utils.initializer import bot
import g4f
import speech_recognition as sr
import subprocess
from utils.options import input_ogg_file, output_wav_file

def convert_audio_to_wav():
    command = f'ffmpeg -y -i {input_ogg_file} {output_wav_file}'
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        return True
    else:
        return False

def recognize_audio_from_file():
    recognizer = sr.Recognizer()
    with sr.AudioFile(output_wav_file) as source:
        audio = recognizer.record(source)
        recognized_text = recognizer.recognize_google(audio, language="ru-RU")
        return recognized_text

def send_typing_action(chat_id):
    bot.send_chat_action(chat_id, 'typing')

def generate_response(user_message):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
    )
    return response

def process_voice_message(voice_data):
    with open(input_ogg_file, "wb") as ogg_file:
        ogg_file.write(voice_data)

    if convert_audio_to_wav():
        recognized_text = recognize_audio_from_file()
        return recognized_text
    return ""
