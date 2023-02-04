import telebot
from telebot import types
bot = telebot.TeleBot('6189070272:AAGodOjSPW6u-Vg_rcvktvJmq3hsshzxRb8')


@bot.message_handler(commands=['help', 'start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Квартиры")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
@bot.message_handler(content_types='text')
def welcome(message):
    if message.text == "Квартиры":
        text="""Квартира с Евро ремонтом рядом с Ривьерой   \
         Адрес: Сибгата Хакима 60 \
         Цена: от 1.600 \
         Спальных мест: 4   \
         Кол-во комнат: 2"""
        text2 = """Уютная квартира рядом с Корстоном    \
         Адрес: Гвардейская 7 \
         Цена: от 1.200 \
         Спальных мест: 5   \
         Кол-во комнат: 2"""
        text3 = """Квартира рядом с центром города \
                 Адрес: Татарстан 66 \
                 Цена: от 1.200 \
                 Спальных мест: 5   \
                 Кол-во комнат: 2"""

        with open('img1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text)
        with open('img1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text2)
        with open('img1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text3)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("1")
        item3 = types.KeyboardButton("2")
        item4 = types.KeyboardButton("3")
        markup2.add(item2)
        markup2.add(item3)
        markup2.add(item4)
        bot.send_message(message.chat.id, 'Выберите квартиру:', reply_markup=markup2)
        #Тут выбор квартиры крч
        if message.text == "1":
            text11 = """Квартира с Евро ремонтом рядом с Ривьерой   \
                    Адрес: Сибгата Хакима 60 \
                    Цена: от 1.600 \
                    Спальных мест: 4   \
                    Кол-во комнат: 2"""
            with open('img1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text)
            item2 = types.KeyboardButton("Фото")
            item3 = types.KeyboardButton("Описание")
            item4 = types.KeyboardButton("Забронировать/посмотреть даты")
            markup2.add(item2)
            markup2.add(item3)
            markup2.add(item4)

bot.infinity_polling()