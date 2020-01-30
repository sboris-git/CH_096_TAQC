import telebot
from tests_api.testHelper import User
import dbconnection
import datetime
bot = telebot.TeleBot('821864551:AAH1yHj0Rvc3x9SZdGR3l-sKMX24l4vriGA')
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока', 'Тесты')
keyboard_tests = telebot.types.ReplyKeyboardMarkup()
keyboard_tests.row('User', 'Category', 'Event', 'Back')
keyboard_user = telebot.types.ReplyKeyboardMarkup(
    row_width=3, resize_keyboard=True)
button_user1 = telebot.types.InlineKeyboardButton(
    text="user edit_username Jesus")
button_user2 = telebot.types.InlineKeyboardButton(text="user back_username")
button_user3 = telebot.types.InlineKeyboardButton(
    text="user edit_birthday 2001-06-04")
button_user4 = telebot.types.InlineKeyboardButton(text="user back_birthday")
button_user5 = telebot.types.InlineKeyboardButton(text="user edit_gender 1")
button_user6 = telebot.types.InlineKeyboardButton(text="user back_gender")
button_user7 = telebot.types.InlineKeyboardButton(text="test back")
keyboard_user.add(
    button_user1,
    button_user3,
    button_user5,
    button_user2,
    button_user4,
    button_user6,
    button_user7)
keyboard_category = telebot.types.ReplyKeyboardMarkup(
    row_width=3, resize_keyboard=True)
button_category1 = telebot.types.InlineKeyboardButton(text="category create_category Hello4")
button_category2 = telebot.types.InlineKeyboardButton(text="category delete_category Hello4")
keyboard_category.add(
    button_category1,
    button_category2,
    button_user7)
users = [360913068, 290088874]
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Зачем ты призвал меня , смертный ?',
        reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    user = User()
    category = dbconnection.Connection()
    if message.text.lower() == 'привет' and message.chat.id == 360913068:
        bot.send_message(message.chat.id, 'Привет мой господин!')
        bot.send_sticker(
            message.chat.id,
            'CAACAgIAAxkBAAMiXjF59f7yXbEXskvdAsHOymOFPDIAAsUCAAJcKIYI81ocvhJ5Qi4YBA')
    elif message.text.lower() == 'привет':
        if message.chat.id == 290088874:
            bot.send_message(
                message.chat.id, 'Привет, пупсик')
        else:
            bot.send_message(
                message.chat.id, 'Привет, {}'.format(
                    message.from_user.first_name))
    elif message.text.lower() == 'пока':
        if message.chat.id == 290088874:
            bot.send_message(
                message.chat.id, 'Прощай, пупсик')
        else:
            bot.send_message(message.chat.id, 'Прощай, путник')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_video(
            message.chat.id,
            open(
                'C:/Users/tolos/Documents/env/CH_096_TAQC/Bot/animation.mp4',
                'rb'))
    elif message.text.lower() == 'тесты':
        bot.send_message(
            message.chat.id,
            'Tests:',
            reply_markup=keyboard_tests)
    elif message.text.lower() == 'back':
        bot.send_message(
            message.chat.id,
            'Main:',
            reply_markup=keyboard)
    elif message.text.lower() == 'test back':
        bot.send_message(message.chat.id, "Back:", reply_markup=keyboard_tests)
    elif message.text.lower().split(' ')[0] == 'user':
        try:
            print(message.text.lower().split()[1])
            if message.text.lower().split()[1] == 'edit_username':
                user.edit_username(message.text.split()[2])
                print(user.get_username())
                bot.send_message(message.chat.id, user.get_username())
            elif message.text.lower().split()[1] == 'back_username':
                user.back_username()
                print(user.get_username())
                bot.send_message(message.chat.id, user.get_username())
            elif message.text.lower().split()[1] == 'edit_birthday':
                user.edit_birthday(message.text.split()[2])
                print(user.get_birthday())
                bot.send_message(message.chat.id, user.get_birthday())
            elif message.text.lower().split()[1] == 'back_birthday':
                user.back_birthday()
                print(user.get_birthday())
                bot.send_message(message.chat.id, user.get_birthday())
            elif message.text.lower().split()[1] == 'edit_gender':
                user.edit_gender(message.text.split()[2])
                print(user.get_gender())
                bot.send_message(message.chat.id, user.get_gender())
            elif message.text.lower().split()[1] == 'back_gender':
                user.back_gender()
                print(user.get_gender())
                bot.send_message(message.chat.id, user.get_gender())
        except BaseException:
            bot.send_message(
                message.chat.id,
                'User:',
                reply_markup=keyboard_user)

    elif message.text.lower().split(' ')[0] == 'category':
        try:
            print(message.text.lower().split()[1])
            if message.text.lower().split()[1] == 'create_category':
                category.create_category_with_name(message.text.split()[2])
                print('Категория {} создана'.format(message.text.split()[2]))
                bot.send_message(message.chat.id, message.text.split()[2])
            elif message.text.lower().split()[1] == 'delete_category':
                category.delete_category_with_name(message.text.split()[2])
                print('Категория {} удалена'.format(message.text.split()[2]))
                bot.send_message(message.chat.id, 'Category {} was deleted'.format(message.text.split()[2]))
            elif message.text.lower().split()[1] == 'edit_category':
                user.edit_birthday(message.text.split()[2])
                print(user.get_birthday())
                bot.send_message(message.chat.id, user.get_birthday())
        except BaseException:
            bot.send_message(
                message.chat.id,
                'Category:',
                reply_markup=keyboard_category)

    else:
        bot.send_message(message.chat.id, 'оу , шо є ?!')

    # Loging
    loger = open('loger.log', "a")
    now = datetime.datetime.now()
    now = '{}:{}:{} {}.{}.{}'.format(
        now.hour,
        now.minute,
        now.second,
        now.day,
        now.month,
        now.year)
    log = 'Time:{}  Id:{}  User:{}  Message: {}'.format(
        now, message.chat.id, message.from_user.first_name, message.text)
    loger.write('\n{}'.format(log))
    print(log)
    loger.close()


@bot.callback_query_handler(func=lambda call: True)
def longname(call):
    if call.data == "user edit_username Jesus":
        bot.send_message(chat_id=360913068, text='оу , шо є ?!')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
