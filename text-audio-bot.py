import telebot
from io import BytesIO
from gtts import gTTS
from numpy.polynomial.laguerre import lagmul

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi, I'm a text-to-audio translation bot. Send me a text and I'll send you a voice message.")

@bot.message_handler(func = lambda message: True)
def text_to_audio(message):
    text = message.text
    tts = gTTS(text, lang='en')
    speech = BytesIO()
    tts.write_to_fp(speech)
    speech.seek(0)
    bot.send_audio(message.chat.id, speech)

bot.polling()