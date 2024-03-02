import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
 
def enviar_mensagem_telegram(mensagem):
    chat_id = 96379830

    print(BOT_TOKEN)

    bot.send_message(chat_id=chat_id, text=mensagem)
