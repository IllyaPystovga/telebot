import telebot
from telebot import types

bot = telebot.TeleBot('5673964448:AAGY5_PZS31TYCELZsa1Ve3dC7gL_1GRmS8')


@bot.message_handler(commands=['start'])
def start(massage):
    mess = f'Привіт, {massage.from_user.first_name} {massage.from_user.last_name}'
    bot.send_message(massage.chat.id, mess)
 # parse_mode='html'


@bot.message_handler(content_types=['text'])
def get_user_text(message):
   if message.text == 'Привіт':
      bot.send_message(message.chat.id, 'I тобі привіт :)')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'твій id: {message.from_user.id}')
    elif message.text == 'скинь фото':
        photo = open('kotik.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
    bot.send_message(message.chat.id, 'йой щось не зрозуміле, спробуй ще раз:)')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, яке гарне фото!')


@bot.message_handler(content_types=['webside'])
def webside(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Глянь ось це краще!', url='https://www.youtube.com/watch?v=o3ost3sxgv4'))
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)

@bot.message_handler(content_types=['help'])
def webside(message):
    markup = types.ReplyKeyboardMarkup()
    webside = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('start')

    markup.add(webside, start)
    bot.send_message(message.chat.id, 'Чим Вам допомогти ?', reply_markup=markdown)

bot.polling(none_stop=True)
