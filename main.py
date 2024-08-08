#введите пожалуйста перед отладкой в терминал вот это "pip install pyTelegramBotAPI"
import telebot
bot = telebot.TeleBot('7460037254:AAGKz-fFy1Wt9yaVW7zyoi-F1byyo3RXw6o')
@bot.message_handler(commands = ['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, это информационный бот лучшей IT-компании')
@bot.message_handler(commands = ['ouryoutube'])
def YouTube_handler(message):
    bot.send_message(message.chat.id, '[Наш YouTube](https://www.youtube.com/@PMC_Fox_skuad/featured)', parse_mode = 'Markdown')
@bot.message_handler(commands = ['ourwebsite'])
def OurWebSite_handler(massage):
    bot.send_message(massage.chat.id, '[Наш WebSite (пока не робит, я забыл продлить хостинг)](http://cw86464.tw1.ru/)', parse_mode = 'Markdown')
@bot.message_handler(commands = ['writetocreator'])
def creator(massage):
    bot.send_message(massage.chat.id, '[для обратной связи:)](https://t.me/mapat221)', parse_mode = 'Markdown')
@bot.message_handler(content_types=["text"])
def user(message):
    if message.text == "/trytogenerateyourname":
        d = bot.send_message(message.chat.id, 'Попробуй создать никнейм для своего бота и отправь мне его, только учти, что он должен оканчиваться на bot, не может начинаться с цифры или содержать более 20 символов')
        bot.register_next_step_handler(d ,cap)
def cap(message):
    global d
    d = message.text
    if d[0] not in '0123456789' and len(d) <= 20 and d[-3:] == 'bot':
        bot.send_message(message.chat.id, "Ник принят, звучит круто")
    else:
        bot.send_message(message.chat.id, "Ошибка в нике, отправь команду заново и попробуй еще раз")
bot.infinity_polling()
