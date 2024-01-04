import telebot
import requests
import json
from config import lzt_token, id_user_lzt, tg_token, payment, contacts, user

bot = telebot.TeleBot(tg_token)

#запрос и получение данных
request = requests.get('https://api.zelenka.guru/users?page='+id_user_lzt+'&limit=1',headers={'Authorization':lzt_token})
data = json.loads(request.text)
username = (data['users'][0]['username'])
user_like_count = (data['users'][0]['user_like_count'])
user_title = (data['users'][0]['user_title'])
permalink = (data['users'][0]['links']['permalink'])
photo = (data['users'][0]['links']['avatar_big'])

#сбор инфы
info = (f'| ZELENKA.GURU |\n\nАватар - {photo}\n'
	 f'Профиль - `{permalink}`\n'
	 f'Ник - `{username}`\n'
	 f'Количество симпатий: `{user_like_count}`\n'
	 f'Статус: `{user_title}`\n\n| {user} |')

contacts = f'lolz - {permalink}\n' + contacts

#отправка в тг
@bot.message_handler(commands=['start'])
def send_lessons(message):
	bot.reply_to(message, info, parse_mode="MARKDOWN")

@bot.message_handler(commands=['payments'])
def send_lessons(message):
	bot.reply_to(message, payment, parse_mode="MARKDOWN")

@bot.message_handler(commands=['contacts'])
def send_lessons(message):
	bot.reply_to(message, contacts)
#говнокодик написан

bot.polling()
