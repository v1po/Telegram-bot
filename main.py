import telebot
from telebot import types
import webbrowser
import json
from bs4 import BeautifulSoup
import datetime

data_now = "2024-05-01"
bot = telebot.TeleBot('7116629033:AAFghZIK-Fj8xyWV2F7bJfq6yPPATZLO4So')
with open('main.json', 'r', encoding='utf8') as f:
    text = json.load(f)
@bot.message_handler(commands=['start'])
def get_start(message):
         markup = types.InlineKeyboardMarkup()
         btn_site = types.InlineKeyboardButton('Website', callback_data='Websait')
         btn_table = types.InlineKeyboardButton('Timetable', callback_data='timetable')
         btn_help = types.InlineKeyboardButton('Help', callback_data='help')
         markup.row(btn_site,btn_table,btn_help)
         bot.reply_to(message,f'Привет {message.from_user.first_name}, я бот с расписание, узнать мои возможности можно в /help или выбрать ниже',reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    for txt in text['schedule']:
        present = (f'{txt['lesson_number']} Урок: {txt['subject']} Учитель: {txt['teacher']} дата и время: {txt['lesson_date']} {txt['from']} - {txt['to']}')
    if callback.data == 'Websait':
        webbrowser.open('https://raspisanie.nikasoft.ru/22811554.html#cls')
    elif callback.data == 'timetable':
        bot.send_message(callback.message.chat.id, "Расписание на сегодня:")
        for txt in text['schedule']:
            if txt['lesson_date'] == "2024-05-03":
                present = (f'{txt['lesson_number']} Урок: {txt['subject']} Учитель: {txt['teacher']} дата и время: {txt['lesson_date']} {txt['from']} - {txt['to']}')
                bot.send_message(callback.message.chat.id, present)
        bot.send_message(callback.message.chat.id, "Расписание на завтра:")
        for txt in text['schedule']:
            if txt['lesson_date'] == "2024-05-04":
                present = (f'{txt['lesson_number']} Урок: {txt['subject']} Учитель: {txt['teacher']} дата и время: {txt['lesson_date']} {txt['from']} - {txt['to']}')
                bot.send_message(callback.message.chat.id, present)
    elif callback.data == "help":
        bot.send_message(callback.message.chat.id, "Бот создан в обучающих целях, у него есть такие возможности как:")

@bot.message_handler(commands=['help'])
def get_help(message):
         bot.send_message(message.chat.id,"Бот создан в обучающих целях, у него есть такие возможности как:")

@bot.message_handler(commands=['opensite'])
def get_opensite(message):
        webbrowser.open('https://raspisanie.nikasoft.ru/22811554.html#cls')

@bot.message_handler(commands=['site'])
def get_site(message):
    markup = types.InlineKeyboardMarkup()
    btn_site = types.InlineKeyboardButton('Перейти на сайт', url='http://raspisanie.nikasoft.ru/22811554.html#cls')
    markup.row(btn_site)
    bot.reply_to(message, "Вот сайт с которого берем информацию", reply_markup=markup)

@bot.message_handler(commands=['timetable'])
def get_timetable(message):
    bot.send_message(message.chat.id, "Расписание на сегодня:")
    for txt in text['schedule']:
        if txt['lesson_date'] == "2024-05-03":
            present = (f'{txt['lesson_number']} Урок: {txt['subject']} Учитель: {txt['teacher']} дата и время: {txt['lesson_date']} {txt['from']} - {txt['to']}')
            bot.send_message(message.chat.id,present)
    bot.send_message(message.chat.id, "Расписание на завтра:")
    for txt in text['schedule']:
        if txt['lesson_date'] == "2024-05-04":
            present = (f'{txt['lesson_number']} Урок: {txt['subject']} Учитель: {txt['teacher']} дата и время: {txt['lesson_date']} {txt['from']} - {txt['to']}')
            bot.send_message(message.chat.id,present )
bot.polling(none_stop=True)
