import telebot

bot = telebot.TeleBot('5673964448:AAGY5_PZS31TYCELZsa1Ve3dC7gL_1GRmS8')


@bot.message_handler(commands=['start'])
def start(massage):
    mess = f'Привіт, {massage.from_user.first_name} {massage.from_user.last_name}'
    bot.send_message(massage.chat.id, mess)
 # parse_mode='html'


@bot.message_handler()
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


bot.polling(none_stop=True)
