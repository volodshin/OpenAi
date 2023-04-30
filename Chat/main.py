from config import API_KEY, BOT_TOKEN
import telebot
import openai


openai.api_key = f'{API_KEY}'
bot = telebot.TeleBot(f"{BOT_TOKEN}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def send_res(message):

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": f"{message.text}"}
    ]
    )
    bot.send_message(message.chat.id, str(response.choices[0].message.content))


bot.infinity_polling()