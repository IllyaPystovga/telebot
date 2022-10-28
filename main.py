import telebot

bot = telebot.TeleBot('5673964448:AAGY5_PZS31TYCELZsa1Ve3dC7gL_1GRmS8')


@bot.message_handler(commands=['start'])
def start(massage):
    mess = f'Привіт, <b>{massage.from_user.first_name} <u>{massage.from_user.last_name}</u><b>'
    bot.send_message(massage.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)
