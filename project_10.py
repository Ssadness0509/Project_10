import telebot 
from telebot import types
bot = telebot.TeleBot('5299587795:AAFyh5vwkxzHCS2soHzQ1nI_8UoVRZYkfKg')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет 👋 , я могу показать тебе твоё расписание.")
    if (message.text == '/start'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("5")
        buttom2 = types.KeyboardButton("6")
        buttom3 = types.KeyboardButton("7")
        buttom4 = types.KeyboardButton("8")         
        buttom5 = types.KeyboardButton("9")
        buttom6 = types.KeyboardButton("10")
        buttom7 = types.KeyboardButton("11")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6, buttom7)
        bot.send_message(message.chat.id, "\n\nВ каком классе ты учишься?", reply_markup=menu)


#----------------------БУКВЫ КЛАССОВ-------------------------------------------------------------------



@bot.message_handler(content_types=['text'])
def get_message(message):

    if (message.text == '5'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("5А")
        buttom2 = types.KeyboardButton("5Б")
        buttom3 = types.KeyboardButton("5В")
        buttom4 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4)
        bot.send_message(message.chat.id, "Теперь уточни букву класса", reply_markup=menu)

    elif (message.text == '6'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("6А")
        buttom2 = types.KeyboardButton("6Б")
        buttom3 = types.KeyboardButton("6В")
        buttom4 = types.KeyboardButton("6Г")
        buttom5 = types.KeyboardButton("6Д")
        buttom6 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Теперь уточни букву класса", reply_markup=menu)
        
    elif (message.text == '7'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("7А")
        buttom2 = types.KeyboardButton("7Б")
        buttom3 = types.KeyboardButton("7В")
        buttom4 = types.KeyboardButton("7Г")
        buttom5 = types.KeyboardButton("7Д")
        buttom6 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Теперь уточни букву класса", reply_markup=menu)
        
    elif (message.text == '8'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("8А")
        buttom2 = types.KeyboardButton("8Б")
        buttom3 = types.KeyboardButton("8В")
        buttom4 = types.KeyboardButton("8Г")
        buttom5 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4,buttom5)
        bot.send_message(message.chat.id, "Теперь уточни букву класса", reply_markup=menu)
        
    elif (message.text == '9'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("9А")
        buttom2 = types.KeyboardButton("9Б")
        buttom3 = types.KeyboardButton("9В")
        buttom4 = types.KeyboardButton("9Г")
        buttom5 = types.KeyboardButton("9Д")
        buttom6 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Теперь уточни букву класса", reply_markup=menu)
        
    elif (message.text == '10'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("10А")
        buttom2 = types.KeyboardButton("10Б")
        buttom3 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3)
        bot.send_message(message.chat.id, "Теперь уточни букву класса", reply_markup=menu)
        
    elif (message.text == '11'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("11А")
        buttom2 = types.KeyboardButton("11Б")
        buttom3 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3,)
        bot.send_message(message.chat.id, "Теперь уточни букву класса", reply_markup=menu)


#----------------------КНОПКА "НАЗАД"-------------------------------------------------------------------


    elif (message.text == 'Назад к классам'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("5")
        buttom2 = types.KeyboardButton("6")
        buttom3 = types.KeyboardButton("7")
        buttom4 = types.KeyboardButton("8")
        buttom5 = types.KeyboardButton("9")
        buttom6 = types.KeyboardButton("10")
        buttom7 = types.KeyboardButton("11")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6, buttom7)
        bot.send_message(message.chat.id, "В каком классе ты учишься?", reply_markup=menu)

    
#----------------------ДНИ-------------------------------------------------------------------



    elif (message.text == '5А'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  5А")
        buttom2 = types.KeyboardButton("Вторник  5А")
        buttom3 = types.KeyboardButton("Среда  5А")
        buttom4 = types.KeyboardButton("Четверг  5А")
        buttom5 = types.KeyboardButton("Пятница  5А")
        buttom6 = types.KeyboardButton("Назад к 5 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '5Б'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  5Б")
        buttom2 = types.KeyboardButton("Вторник  5Б")
        buttom3 = types.KeyboardButton("Среда  5Б")
        buttom4 = types.KeyboardButton("Четверг  5Б")
        buttom5 = types.KeyboardButton("Пятница  5Б")
        buttom6 = types.KeyboardButton("Назад к 5 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '5В'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  5В")
        buttom2 = types.KeyboardButton("Вторник  5В")
        buttom3 = types.KeyboardButton("Среда  5В")
        buttom4 = types.KeyboardButton("Четверг  5В")
        buttom5 = types.KeyboardButton("Пятница  5В")
        buttom6 = types.KeyboardButton("Назад к 5 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '6А'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  6А")
        buttom2 = types.KeyboardButton("Вторник  6А")
        buttom3 = types.KeyboardButton("Среда  6А")
        buttom4 = types.KeyboardButton("Четверг  6А")
        buttom5 = types.KeyboardButton("Пятница  6А")
        buttom6 = types.KeyboardButton("Назад к 6 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '6Б'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  6Б")
        buttom2 = types.KeyboardButton("Вторник  6Б")
        buttom3 = types.KeyboardButton("Среда  6Б")
        buttom4 = types.KeyboardButton("Четверг  6Б")
        buttom5 = types.KeyboardButton("Пятница  6Б")
        buttom6 = types.KeyboardButton("Назад к 6 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '6В'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  6В")
        buttom2 = types.KeyboardButton("Вторник  6В")
        buttom3 = types.KeyboardButton("Среда  6В")
        buttom4 = types.KeyboardButton("Четверг  6В")
        buttom5 = types.KeyboardButton("Пятница  6В")
        buttom6 = types.KeyboardButton("Назад к 6 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '6Г'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  6Г")
        buttom2 = types.KeyboardButton("Вторник  6Г")
        buttom3 = types.KeyboardButton("Среда  6Г")
        buttom4 = types.KeyboardButton("Четверг  6Г")
        buttom5 = types.KeyboardButton("Пятница  6Г")
        buttom6 = types.KeyboardButton("Назад к 6 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '6Д'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  6Д")
        buttom2 = types.KeyboardButton("Вторник  6Д")
        buttom3 = types.KeyboardButton("Среда  6Д")
        buttom4 = types.KeyboardButton("Четверг  6Д")
        buttom5 = types.KeyboardButton("Пятница  6Д")
        buttom6 = types.KeyboardButton("Назад к 6 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '7А'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  7А")
        buttom2 = types.KeyboardButton("Вторник  7А")
        buttom3 = types.KeyboardButton("Среда  7А")
        buttom4 = types.KeyboardButton("Четверг  7А")
        buttom5 = types.KeyboardButton("Пятница  7А")
        buttom6 = types.KeyboardButton("Назад к 7 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '7Б'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  7Б")
        buttom2 = types.KeyboardButton("Вторник  7Б")
        buttom3 = types.KeyboardButton("Среда  7Б")
        buttom4 = types.KeyboardButton("Четверг  7Б")
        buttom5 = types.KeyboardButton("Пятница  7Б")
        buttom6 = types.KeyboardButton("Назад к 7 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '7В'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  7В")
        buttom2 = types.KeyboardButton("Вторник  7В")
        buttom3 = types.KeyboardButton("Среда  7В")
        buttom4 = types.KeyboardButton("Четверг  7В")
        buttom5 = types.KeyboardButton("Пятница  7В")
        buttom6 = types.KeyboardButton("Назад к 7 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '7Г'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  7Г")
        buttom2 = types.KeyboardButton("Вторник  7Г")
        buttom3 = types.KeyboardButton("Среда  7Г")
        buttom4 = types.KeyboardButton("Четверг  7Г")
        buttom5 = types.KeyboardButton("Пятница  7Г")
        buttom6 = types.KeyboardButton("Назад к 7 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '7Д'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  7Д")
        buttom2 = types.KeyboardButton("Вторник  7Д")
        buttom3 = types.KeyboardButton("Среда  7Д")
        buttom4 = types.KeyboardButton("Четверг  7Д")
        buttom5 = types.KeyboardButton("Пятница  7Д")
        buttom6 = types.KeyboardButton("Назад к 7 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '8А'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  8А")
        buttom2 = types.KeyboardButton("Вторник  8А")
        buttom3 = types.KeyboardButton("Среда  8А")
        buttom4 = types.KeyboardButton("Четверг  8А")
        buttom5 = types.KeyboardButton("Пятница  8А")
        buttom6 = types.KeyboardButton("Назад к 8 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '8Б'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  8Б")
        buttom2 = types.KeyboardButton("Вторник  8Б")
        buttom3 = types.KeyboardButton("Среда  8Б")
        buttom4 = types.KeyboardButton("Четверг  8Б")
        buttom5 = types.KeyboardButton("Пятница  8Б")
        buttom6 = types.KeyboardButton("Назад к 8 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '8В'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  8В")
        buttom2 = types.KeyboardButton("Вторник  8В")
        buttom3 = types.KeyboardButton("Среда  8В")
        buttom4 = types.KeyboardButton("Четверг  8В")
        buttom5 = types.KeyboardButton("Пятница  8В")
        buttom6 = types.KeyboardButton("Назад к 8 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '8Г'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  8Г")
        buttom2 = types.KeyboardButton("Вторник  8Г")
        buttom3 = types.KeyboardButton("Среда  8Г")
        buttom4 = types.KeyboardButton("Четверг  8Г")
        buttom5 = types.KeyboardButton("Пятница  8Г")
        buttom6 = types.KeyboardButton("Назад к 8 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '9А'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  9А")
        buttom2 = types.KeyboardButton("Вторник  9А")
        buttom3 = types.KeyboardButton("Среда  9А")
        buttom4 = types.KeyboardButton("Четверг  9А")
        buttom5 = types.KeyboardButton("Пятница  9А")
        buttom6 = types.KeyboardButton("Назад к 9 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '9Б'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  9Б")
        buttom2 = types.KeyboardButton("Вторник  9Б")
        buttom3 = types.KeyboardButton("Среда  9Б")
        buttom4 = types.KeyboardButton("Четверг  9Б")
        buttom5 = types.KeyboardButton("Пятница  9Б")
        buttom6 = types.KeyboardButton("Назад к 9 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '9В'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  9В")
        buttom2 = types.KeyboardButton("Вторник  9В")
        buttom3 = types.KeyboardButton("Среда  9В")
        buttom4 = types.KeyboardButton("Четверг  9В")
        buttom5 = types.KeyboardButton("Пятница  9В")
        buttom6 = types.KeyboardButton("Назад к 9 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '9Г'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  9Г")
        buttom2 = types.KeyboardButton("Вторник  9Г")
        buttom3 = types.KeyboardButton("Среда  9Г")
        buttom4 = types.KeyboardButton("Четверг  9Г")
        buttom5 = types.KeyboardButton("Пятница  9Г")
        buttom6 = types.KeyboardButton("Назад к 9 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '9Д'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  9Д")
        buttom2 = types.KeyboardButton("Вторник  9Д")
        buttom3 = types.KeyboardButton("Среда  9Д")
        buttom4 = types.KeyboardButton("Четверг  9Д")
        buttom5 = types.KeyboardButton("Пятница  9Д")
        buttom6 = types.KeyboardButton("Назад к 9 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '10А'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  10А")
        buttom2 = types.KeyboardButton("Вторник  10А")
        buttom3 = types.KeyboardButton("Среда  10А")
        buttom4 = types.KeyboardButton("Четверг  10А")
        buttom5 = types.KeyboardButton("Пятница  10А")
        buttom6 = types.KeyboardButton("Назад к 10 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '10Б'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  10Б")
        buttom2 = types.KeyboardButton("Вторник  10Б")
        buttom3 = types.KeyboardButton("Среда  10Б")
        buttom4 = types.KeyboardButton("Четверг  10Б")
        buttom5 = types.KeyboardButton("Пятница  10Б")
        buttom6 = types.KeyboardButton("Назад к 10 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)


    elif (message.text == '11А'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  11А")
        buttom2 = types.KeyboardButton("Вторник  11А")
        buttom3 = types.KeyboardButton("Среда  11А")
        buttom4 = types.KeyboardButton("Четверг  11А")
        buttom5 = types.KeyboardButton("Пятница  11А")
        buttom6 = types.KeyboardButton("Назад к 11 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '11Б'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  11Б")
        buttom2 = types.KeyboardButton("Вторник  11Б")
        buttom3 = types.KeyboardButton("Среда  11Б")
        buttom4 = types.KeyboardButton("Четверг  11Б")
        buttom5 = types.KeyboardButton("Пятница  11Б")
        buttom6 = types.KeyboardButton("Назад к 11 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '11В'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  11В")
        buttom2 = types.KeyboardButton("Вторник  11В")
        buttom3 = types.KeyboardButton("Среда  11В")
        buttom4 = types.KeyboardButton("Четверг  11В")
        buttom5 = types.KeyboardButton("Пятница  11В")
        buttom6 = types.KeyboardButton("Назад к 11 классу")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)

    elif (message.text == '11Г'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("Понедельник  11Г")
        buttom2 = types.KeyboardButton("Вторник  11Г")
        buttom3 = types.KeyboardButton("Среда  11Г")
        buttom4 = types.KeyboardButton("Четверг  11Г")
        buttom5 = types.KeyboardButton("Пятница  11Г")
        buttom6 = types.KeyboardButton("Назад к 11 классу ")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=menu)


#----------------------НАЗАД К ВЫБОРУ БУКВЫ КЛАССА-------------------------------------------------------------------


    elif (message.text == 'Назад к 5 классу'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("5А")
        buttom2 = types.KeyboardButton("5Б")
        buttom3 = types.KeyboardButton("5В")
        buttom4 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4)
        bot.send_message(message.chat.id, " уточни букву класса", reply_markup=menu)

    elif (message.text == 'Назад к 6 классу'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("6А")
        buttom2 = types.KeyboardButton("6Б")
        buttom3 = types.KeyboardButton("6В")
        buttom4 = types.KeyboardButton("6Г")
        buttom5 = types.KeyboardButton("6Д")
        buttom6 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, " уточни букву класса", reply_markup=menu)

    elif (message.text == 'Назад к 7 классу'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("7А")
        buttom2 = types.KeyboardButton("7Б")
        buttom3 = types.KeyboardButton("7В")
        buttom4 = types.KeyboardButton("7Г")
        buttom5 = types.KeyboardButton("7Д")
        buttom6 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6 )
        bot.send_message(message.chat.id, " уточни букву класса", reply_markup=menu)

    elif (message.text == 'Назад к 8 классу'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("8А")
        buttom2 = types.KeyboardButton("8Б")
        buttom3 = types.KeyboardButton("8В")
        buttom4 = types.KeyboardButton("8Г")
        buttom5 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4,buttom5)
        bot.send_message(message.chat.id, " уточни букву класса", reply_markup=menu)

    elif (message.text == 'Назад к 9 классу'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("9А")
        buttom2 = types.KeyboardButton("9Б")
        buttom3 = types.KeyboardButton("9В")
        buttom4 = types.KeyboardButton("9Г")
        buttom5 = types.KeyboardButton("9Д")
        buttom6 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3, buttom4, buttom5, buttom6)
        bot.send_message(message.chat.id, " уточни букву класса", reply_markup=menu)

    elif (message.text == 'Назад к 10 классу'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("10А")
        buttom2 = types.KeyboardButton("10Б")
        buttom3 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3,)
        bot.send_message(message.chat.id, " уточни букву класса", reply_markup=menu)

    elif (message.text == 'Назад к 11 классу'):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttom1 = types.KeyboardButton("11А")
        buttom2 = types.KeyboardButton("11Б")
        buttom3 = types.KeyboardButton("Назад к классам")
        menu.add(buttom1, buttom2, buttom3)
        bot.send_message(message.chat.id, " уточни букву класса", reply_markup=menu)



#----------------------РАСПИСАНИЕ-------------------------------------------------------------------
    #----------------------------------------------5А-----------------------------------------------------------
    elif (message.text == 'Понедельник  5А'):
        bot.send_message(message.chat.id, "1. Литература.\n🕒 8:30 - 9:15.\n🚪 41\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 41\n\n3. ИЗО.\n🕒 10:20 - 11:05.\n🚪 41\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 41\n\n5. Биология.\n🕒 12:30 - 13:15.\n🚪 41\n\n6 История.\n🕒 13:25 - 14:10.\n🚪 41\n" )

    elif (message.text == 'Вторник  5А'):
        bot.send_message(message.chat.id, "1. Русский язык.\n🕒 8:30 - 9:15.\n🚪 41\n\n2. ОДНКНР.\n🕒 9:25 - 10:10.\n🚪 41\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 41\n\n4. Физ-ра.\n🕒 11:25 - 12:10.\n🚪 41\n\n5. География\n🕒 12:30 - 13:15.\n🚪 41\n\n6. Естествознание.\n🕒 13:25 - 14:10.\n🚪 41\n" )

    elif (message.text == 'Среда  5А'):
        bot.send_message(message.chat.id, "1. Инф./Англ. Яз\n🕒 8:30 - 9:15.\n🚪 41\n\n2. Инф./Англ. Яз.\n🕒 9:25 - 10:10.\n🚪 41\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 41\n\n4. Музыка.\n🕒 11:25 - 12:10.\n🚪 41\n\n5. Родной язык.\n🕒 12:30 - 13:15.\n🚪 41\n\n6. Родная литература.\n🕒 13:25 - 14:10.\n🚪 41\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 41" )

    elif (message.text == 'Четверг  5А'):
        bot.send_message(message.chat.id, "1. Русский язык.\n🕒 8:30 - 9:15.\n🚪 41\n\n2. Английский язык.\n🕒 9:25 - 10:10.\n🚪 41\n\n3. Технология.\n🕒 10:20 - 11:05.\n🚪 41\n\n4. Технология.\n🕒 11:25 - 12:10.\n🚪 41\n\n5. История.\n🕒 12:30 - 13:15.\n🚪 41\n\n6. Математика.\n🕒 13:25 - 14:10.\n🚪 41\n" )

    elif (message.text == 'Пятница  5А'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n🚪 41\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 41\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 41\n\n4. Литература.\n🕒 11:25 - 12:10.\n🚪 41\n\n5. Английский язык.\n🕒 12:30 - 13:15.\n🚪 41" )

      #----------------------------------------------5Б-----------------------------------------------------------
    elif (message.text == 'Понедельник  5Б'):
        bot.send_message(message.chat.id, "1. Музыка.\n🕒 8:30 - 9:15.\n🚪 40\n\n2. Инф./Англ.\n🕒 9:25 - 10:10.\n🚪 29 и 40\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 40\n\n4. Биология.\n🕒 11:25 - 12:10.\n🚪 40\n\n5. Русский язык.\n🕒 12:30 - 13:15.\n🚪 40\n\n6. ОДНКНР.\n🕒 13:25 - 14:10.\n🚪 40\n" )

    elif (message.text == 'Вторник  5Б'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n🚪 40\n\n2. История.\n🕒 9:25 - 10:10.\n🚪 40\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 40\n\n4. Инф./Англ.\n🕒 11:25 - 12:10.\n🚪 29 и 40\n\n5. Естествознание\n🕒 12:30 - 13:15.\n🚪 40\n\n6. Математика.\n🕒 13:25 - 14:10.\n🚪 40\n" )

    elif (message.text == 'Среда  5Б'):
        bot.send_message(message.chat.id, "1. Литература.\n🕒 8:30 - 9:15.\n🚪 40\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 40\n\n3. Английский язык.\n🕒 10:20 - 11:05.\n🚪 40 и 48\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 40\n\n5. ИЗО.\n🕒 12:30 - 13:15.\n🚪 40\n\n6. География.\n🕒 13:25 - 14:10.\n🚪 40\n" )

    elif (message.text == 'Четверг  5Б'):
        bot.send_message(message.chat.id, "1. Технология.\n🕒 8:30 - 9:15.\n🚪 40 и 10\n\n2. Технология.\n🕒 9:25 - 10:10.\n🚪 40 и 10\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 40\n\n4. Литература.\n🕒 11:25 - 12:10.\n🚪 40\n\n5. Математика.\n🕒 12:30 - 13:15.\n🚪 40\n\n6. Английский язык.\n🕒 13:25 - 14:10.\n🚪 40 и 42\n" )

    elif (message.text == 'Пятница  5Б'):
        bot.send_message(message.chat.id, "1. Родной русский.\n🕒 8:30 - 9:15.\n🚪 40\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n🚪 Спорт. зал\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 40\n\n4. История.\n🕒 11:25 - 12:10.\n🚪 40\n\n5. Родная литература.\n🕒 12:30 - 13:15.\n🚪 40\n\n6. Классный час.\n🕒 14:20 - 15:05." )

#----------------------------------------------5В-----------------------------------------------------------
    elif (message.text == 'Понедельник  5В'):
        bot.send_message(message.chat.id, "1. Технология.\n🕒 8:30 - 9:15.\n🚪 21 и 10\n\n2. Технология.\n🕒 9:25 - 10:10.\n🚪 21 и 10\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 21\n\n4. Родной язык.\n🕒 11:25 - 12:10.\n🚪 21\n\n5. Родная литература.\n🕒 12:30 - 13:15.\n🚪 21\n\n6. Биология.\n🕒 13:25 - 14:10.\n🚪 21\n\n\n" )

    elif (message.text == 'Вторник  5В'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n🚪 21\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n🚪 Спорт. зал\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 21\n\n4. Естествознание.\n🕒 11:25 - 12:10.\n🚪 21\n\n5. Литература.\n🕒 12:30 - 13:15.\n🚪 21\n\n6. Математика.\n🕒 13:25 - 14:10.\n🚪 21\n\n")

    elif (message.text == 'Среда  5В'):
        bot.send_message(message.chat.id, "1. Литература.\n🕒 8:30 - 9:15.\n🚪 21\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 21\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 21\n\n4. Инф./Англ.\n🕒 11:25 - 12:10.\n🚪 29 и 21\n\n5. Инф./Англ.\n🕒 12:30 - 13:15.\n🚪 29 и 21\n\n6. Музыка.\n🕒 13:25 - 14:10.\n🚪 21\n\n" )

    elif (message.text == 'Четверг  5В'):
        bot.send_message(message.chat.id, "1. Математика.\n🕒 8:30 - 9:15.\n🚪 21\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 21\n\n3. Английский язык.\n🕒 10:20 - 11:05.\n🚪 21 и 30\n\n4. Русский язык.\n🕒 11:25 - 12:10.\n🚪 21\n\n5. История.\n🕒 12:30 - 13:15.\n🚪 21\n\n6. ИЗО.\n🕒 13:25 - 14:10.\n🚪 21\n\n" )

    elif (message.text == 'Пятница  5В'):
        bot.send_message(message.chat.id, "1. Английский язык.\n🕒 8:30 - 9:15.\n🚪 21 и 48\n\n2. География.\n🕒 9:25 - 10:10.\n🚪 21\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n🚪 Спорт. зал\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 21\n\n5. ОДНКНР.\n🕒 12:30 - 13:15.\n🚪 21\n\n6. Классный час.\n🕒 14:20 - 15:05.\n🚪 21\n\n" )

   #----------------------------------------------6А-----------------------------------------------------------
    elif (message.text == 'Понедельник  6А'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n🚪 50\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 50\n\n3. Английский язык.\n🕒 10:20 - 11:05.\n🚪 50 и 42\n\n4. Русский язык.\n🕒 11:25 - 12:10.\n🚪 50\n\n5. ИЗО.\n🕒 12:30 - 13:15.\n🚪 50\n\n6. Литература.\n🕒 13:25 - 14:10.\n🚪 50")

    elif (message.text == 'Вторник  6А'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n🚪 Спорт. зал\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 50\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 50\n\n4. Музыка.\n🕒 11:25 - 12:10.\n🚪 50\n\n5. Инф./Англ.\n🕒 12:30 - 13:15.\n🚪 29 и 50\n\n6. Инф./Англ.\n🕒 13:25 - 14:10.\n🚪 29 и 50\n\n7. Классный час.\n🕒 14:20 - 15:05..")

    elif (message.text == 'Среда  6А'):
        bot.send_message(message.chat.id, "1. Русский язык.\n🕒 8:30 - 9:15.\n🚪 50\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 50\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 50\n\n4. Биология.\n🕒 11:25 - 12:10.\n🚪 50\n\n5. География.\n🕒 12:30 - 13:15.\n🚪 50\n\n6. Обществознание.\n🕒 13:25 - 14:10.\n🚪 50")

    elif (message.text == 'Четверг  6А'):
        bot.send_message(message.chat.id, "1. Математика.\n🕒 8:30 - 9:15.\n🚪 50\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 50\n\n3. Литература.\n🕒 10:20 - 11:05.\n🚪 50\n\n4. История.\n🕒 11:25 - 12:10.\n🚪 50\n\n5. Естествознание.\n🕒 12:30 - 13:15.\n🚪 50\n\n6. Физ-ра.\n🕒 13:25 - 14:10.\n🚪 Спорт. зал")

    elif (message.text == 'Пятница  6А'):
        bot.send_message(message.chat.id, "1. Технология.\n🕒 8:30 - 9:15.\n🚪 50 и 10\n\n2. Технология.\n🕒 9:25 - 10:10.\n🚪 50 и 10\n\n3. Английский язык.\n🕒 10:20 - 11:05.\n🚪 50 и 48\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 50\n\n5. Родной язык.\n🕒 12:30 - 13:15.\n🚪 50\n\n6. Родная литература.\n🕒 13:25 - 14:10.\n🚪 50")

#----------------------------------------------6Б-----------------------------------------------------------
    elif (message.text == 'Понедельник  6Б'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n🚪 Спорт. зал\n\n2. История.\n🕒 9:25 - 10:10.\n🚪 44\n\n3. Инф./Англ.\n🕒 10:20 - 11:05.\n🚪 29 и44\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 44\n\n5. Русский язык.\n🕒 12:30 - 13:15.\n🚪 44\n\n6. Литература.\n🕒 13:25 - 14:10.\n🚪 44")

    elif (message.text == 'Вторник  6Б'):
        bot.send_message(message.chat.id, "1. Инф./Англ.\n🕒 8:30 - 9:15.\n🚪 29 и 44\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 44\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 44\n\n4. Технология.\n🕒 11:25 - 12:10.\n🚪 44 и 10\n\n5. Технология.\n🕒 12:30 - 13:15.\n🚪 44 и 10\n\n6. Математика.\n🕒 13:25 - 14:10.\n🚪 44")

    elif (message.text == 'Среда  6Б'):
        bot.send_message(message.chat.id, "1. Русский язык.\n🕒 8:30 - 9:15.\n🚪 44\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 44\n\n3. Обществознание.\n🕒 10:20 - 11:05.\n🚪 44\n\n4. Физ-ра.\n🕒 11:25 - 12:10.\n🚪 Спорт. зал\n\n5. Естествознание.\n🕒 12:30 - 13:15.\n🚪 44\n\n6. Английский язык.\n🕒 13:25 - 14:10.\n🚪 44 и 42")

    elif (message.text == 'Четверг  6Б'):
        bot.send_message(message.chat.id, "1. Литература.\n🕒 8:30 - 9:15.\n🚪 44\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 44\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 44\n\n4. География.\n🕒 11:25 - 12:10.\n🚪 44\n\n5. Английский язык.\n🕒 12:30 - 13:15.\n🚪 44 и 29\n\n6. Музыка.\n🕒 13:25 - 14:10.\n🚪 44\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 44")

    elif (message.text == 'Пятница  6Б'):
        bot.send_message(message.chat.id, "1. Родная литература.\n🕒 8:30 - 9:15.\n🚪 44\n\n2. История.\n🕒 9:25 - 10:10.\n🚪 44\n\n3. Родной язык.\n🕒 10:20 - 11:05.\n🚪 44\n\n4. ИЗО.\n🕒 11:25 - 12:10.\n🚪 44\n\n5. Биология.\n🕒 12:30 - 13:15.\n🚪 44\n\n6. Математика.\n🕒 13:25 - 14:10.\n🚪 44")

#----------------------------------------------6В-----------------------------------------------------------
    elif (message.text == 'Понедельник  6В'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n🚪 45\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 45\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n🚪 Спорт. зал\n\n4. Инф./Англ.\n🕒 11:25 - 12:10.\n🚪 29 и 45\n\n5. Русский язык.\n🕒 12:30 - 13:15.\n🚪 45\n\n6. Литература.\n🕒 13:25 - 14:10.\n🚪 45")

    elif (message.text == 'Вторник  6В'):
        bot.send_message(message.chat.id, "1. Обществознание.\n🕒 8:30 - 9:15.\n🚪 45\n\n2. Инф./Англ.\n🕒 9:25 - 10:10.\n🚪 29 и 45\n\n3. Родной язык.\n🕒 10:20 - 11:05.\n🚪 45\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 45\n\n5. Естествознание.\n🕒 12:30 - 13:15.\n🚪 45\n\n6. Родная литература.\n🕒 13:25 - 14:10.\n🚪 45")

    elif (message.text == 'Среда  6В'):
        bot.send_message(message.chat.id, "1. Математика.\n🕒 8:30 - 9:15.\n🚪 45\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 45\n\n3. Технология.\n🕒 10:20 - 11:05.\n🚪 45 и 10\n\n4. Технология.\n🕒 11:25 - 12:10.\n🚪 45 и 10\n\n5. Английский язык.\n🕒 12:30 - 13:15.\n🚪 45 и 42\n\n6. Физ-ра.\n🕒 13:25 - 14:10.\n🚪 Спорт. зал")

    elif (message.text == 'Четверг  6В'):
        bot.send_message(message.chat.id, "1. ИЗО.\n🕒 8:30 - 9:15.\n🚪 45\n\n2. Русский язык.\n🕒 9:25 - 10:10.\n🚪 45\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 45\n\n4. Английский язык.\n🕒 11:25 - 12:10.\n🚪 45 и 29\n\n5. География.\n🕒 12:30 - 13:15.\n🚪 45\n\n6. Русский язык.\n🕒 13:25 - 14:10.\n🚪 45\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 45")

    elif (message.text == 'Пятница  6В'):
        bot.send_message(message.chat.id, "1. Литература.\n🕒 8:30 - 9:15.\n🚪 45\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 45\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 45\n\n4. Биология.\n🕒 11:25 - 12:10.\n🚪 45\n\n5. История.\n🕒 12:30 - 13:15.\n🚪 45\n\n6. Музыка.\n🕒 13:25 - 14:10.\n🚪 45")


#----------------------------------------------6Г-----------------------------------------------------------
    elif (message.text == 'Понедельник  6Г'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n🚪 46\n\n2. Родной язык.\n🕒 9:25 - 10:10.\n🚪 46\n\n3. Технология.\n🕒 10:20 - 11:05.\n🚪 46 и 10\n\n4. Технология.\n🕒 11:25 - 12:10.\n🚪 46 и 10\n\n5. Математика.\n🕒 12:30 - 13:15.\n🚪 46\n\n6. Биология.\n🕒 13:25 - 14:10.\n🚪 46")

    elif (message.text == 'Вторник  6Г'):
        bot.send_message(message.chat.id, "1. Математика.\n🕒 8:30 - 9:15.\n🚪 46\n\n2. Английский язык.\n🕒 9:25 - 10:10.\n🚪 46 и 30\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n🚪 Спорт. зал\n\n4. География.\n🕒 11:25 - 12:10.\n🚪 46\n\n5. Русский язык.\n🕒 12:30 - 13:15.\n🚪 46\n\n6. Литература.\n🕒 13:25 - 14:10.\n🚪 46")

    elif (message.text == 'Среда  6Г'):
        bot.send_message(message.chat.id, "1. Русский язык.\n🕒 8:30 - 9:15.\n🚪 46\n\n2. Обществознание.\n🕒 9:25 - 10:10.\n🚪 46\n\n3. Русский язык.\n🕒 10:20 - 11:05.\n🚪 46\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 46\n\n5. Музыка.\n🕒 12:30 - 13:15.\n🚪 46\n\n6. Естествознание.\n🕒 13:25 - 14:10.\n🚪 46")

    elif (message.text == 'Четверг  6Г'):
        bot.send_message(message.chat.id, "1. Инф./Англ.\n🕒 8:30 - 9:15.\n🚪 29 и 46\n\n2. Инф./Англ.\n🕒 9:25 - 10:10.\n🚪 29 и 46\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 46\n\n4. Русский язык.\n🕒 11:25 - 12:10.\n🚪 46\n\n5. Физ-ра.\n🕒 12:30 - 13:15.\n🚪 46\n\n6. Литература.\n🕒 13:25 - 14:10.\n🚪 46\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 46")

    elif (message.text == 'Пятница  6Г'):
        bot.send_message(message.chat.id, "1. Русский язык.\n🕒 8:30 - 9:15.\n🚪 46\n\n2. Английский язык.\n🕒 9:25 - 10:10.\n🚪 46 и 29\n\n3. ИЗО.\n🕒 10:20 - 11:05.\n🚪 46\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 46\n\n5. История.\n🕒 12:30 - 13:15.\n🚪 46\n\n6. Родная литература.\n🕒 13:25 - 14:10.\n🚪 46")
        
#----------------------------------------------6Д-----------------------------------------------------------

    elif (message.text == 'Понедельник  6Д'):
        bot.send_message(message.chat.id, "1. Литература.\n🕒 8:30 - 9:15.\n🚪 54\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n🚪 Спорт. зал\n\n3. История.\n🕒 10:20 - 11:05.\n🚪 54\n\n4. Русский язык.\n🕒 11:25 - 12:10.\n🚪 54\n\n5. Естествознание.\n🕒 12:30 - 13:15.\n🚪 54\n\n6. Математика.\n🕒 13:25 - 14:10.\n🚪 54")

    elif (message.text == 'Вторник  6Д'):
        bot.send_message(message.chat.id, "1. География.\n🕒 8:30 - 9:15.\n🚪 54\n\n2. Математика.\n🕒 9:25 - 10:10.\n🚪 54\n\n3. Инф./Англ.\n🕒 10:20 - 11:05.\n🚪 29 и 54\n\n4. Родной язык.\n🕒 11:25 - 12:10.\n🚪 54\n\n5. Родная литература.\n🕒 12:30 - 13:15.\n🚪 54\n\n6. Музыка.\n🕒 13:25 - 14:10.\n🚪 54\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 54")

    elif (message.text == 'Среда  6Д'):
        bot.send_message(message.chat.id, "1. Английский язык.\n🕒 8:30 - 9:15.\n🚪 54 и 42\n\n2. Обществознание.\n🕒 9:25 - 10:10.\n🚪 54\n\n3. Математика.\n🕒 10:20 - 11:05.\n🚪 54\n\n4. Русский язык.\n🕒 11:25 - 12:10.\n🚪 54\n\n5. Физ-ра.\n🕒 12:30 - 13:15.\n🚪 Спорт. зал\n\n6. Литература.\n🕒 13:25 - 14:10.\n🚪 54")

    elif (message.text == 'Четверг  6Д'):
        bot.send_message(message.chat.id, "1. Литература.\n🕒 8:30 - 9:15.\n🚪 54\n\n2. ИЗО.\n🕒 9:25 - 10:10.\n🚪 54\n\n3. Инф./Англ.\n🕒 10:20 - 11:05.\n🚪 29 и 54\n\n4. Математика.\n🕒 11:25 - 12:10.\n🚪 54\n\n5. Русский язык.\n🕒 12:30 - 13:15.\n🚪 54\n\n6. История.\n🕒 13:25 - 14:10.\n🚪 54")

    elif (message.text == 'Пятница  6Д'):
        bot.send_message(message.chat.id, "1. Английский язык.\n🕒 8:30 - 9:15.\n🚪 54 и 29\n\n2. Биология.\n🕒 9:25 - 10:10.\n🚪 54\n\n3. Технология.\n🕒 10:20 - 11:05.\n🚪 54 и 10\n\n4. Технология.\n🕒 11:25 - 12:10.\n🚪 54 и 10\n\n5. Математика.\n🕒 12:30 - 13:15.\n🚪 54\n\n6. Русский язык.\n🕒 13:25 - 14:10.\n🚪 54")

    #----------------------------------------------7А-----------------------------------------------------------
    elif (message.text == 'Понедельник  7А'):
        bot.send_message(message.chat.id, "1. Лит-ра.\n🕒 8:30 - 9:15.\n🚪 33\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 33\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n🚪 33\n\n4. История.\n🕒 11:25 - 12:10.\n🚪 33\n\n5. География.\n🕒 12:30 - 13:15.\n🚪 33\n\n6. Тех./Англ.\n🕒 13:25 - 14:10.\n🚪 48 и 33\n\n7. Тех./Англ.\n🕒 14:20 - 15:05.\n🚪 48 и 33\n\n")

    elif (message.text == 'Вторник  7А'):
        bot.send_message(message.chat.id, "1. Биология.\n🕒 8:30 - 9:15.\n🚪 33\n\n2. Физика.\n🕒 9:25 - 10:10.\n🚪 33\n\n3. Музыка.\n🕒 10:20 - 11:05.\n🚪 33\n\n4. Англ. яз.\n🕒 11:25 - 12:10.\n🚪 33 и 42\n\n5. Нем./Кит .\n🕒 12:30 - 13:15.\n🚪 33 и 48\n\n6. Рус. яз.\n🕒 13:25 - 14:10.\n🚪 33")

    elif (message.text == 'Среда  7А'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n🚪 33\n\n2. Рус. яз.\n🕒 9:25 - 10:10.\n🚪 33\n\n3. Геометрия.\n🕒 10:20 - 11:05.\n🚪 33\n\n4. Лит-ра.\n🕒 11:25 - 12:10.\n🚪 33\n\n5. Физ-ра.\n🕒 12:30 - 13:15.\n🚪 Спорт. зал\n\n6. Обществознание.\n🕒 13:25 - 14:10.\n🚪 33\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 33")

    elif (message.text == 'Четверг  7А'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n🚪 33\n\n2. География.\n🕒 9:25 - 10:10.\n🚪 33\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n🚪 33\n\n4. Геометрия.\n🕒 11:25 - 12:10.\n🚪 33\n\n5. ИЗО.\n🕒 12:30 - 13:15.\n🚪 33\n\n6. Физика.\n🕒 13:25 - 14:10.\n🚪 33")

    elif (message.text == 'Пятница  7А'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n🚪 33\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 33\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n🚪 Спорт. зал\n\n4. Химия.\n🕒 11:25 - 12:10.\n🚪 33\n\n5. Информат.\n🕒 12:30 - 13:15.\n🚪 29 и 33\n\n6. Тех./Англ.\n🕒 13:25 - 14:10.\n🚪 48 и 33\n\n7. Тех./Англ.\n🕒 14:20 - 15:05.\n🚪 48 и 33\n\n")


     #----------------------------------------------7Б-----------------------------------------------------------

    elif (message.text == 'Понедельник  7Б'):
        bot.send_message(message.chat.id, "1. Рус. яз.\n🕒 8:30 - 9:15.\n🚪 36\n\n2. История.\n🕒 9:25 - 10:10.\n🚪 36\n\n3. Геометрия.\n🕒 10:20 - 11:05.\n🚪 36\n\n4. География.\n🕒 11:25 - 12:10.\n🚪 36\n\n5. Информат.\n🕒 12:30 - 13:15.\n🚪 29 и 36\n\n6. Тех./Кит.\n🕒 13:25 - 14:10.\n🚪 39 и 36\n\n7. Тех./Фр.\n🕒 14:20 - 15:05.\n🚪 39 и 36")

    elif (message.text == 'Вторник  7Б'):
        bot.send_message(message.chat.id, "1. Лит-ра.\n🕒 8:30 - 9:15.\n🚪 36\n\n2. Англ. яз.\n🕒 9:25 - 10:10.\n🚪 36 и библиотека\n\n3. Геометрия.\n🕒 10:20 - 11:05.\n🚪 36\n\n4. Рус. яз.\n🕒 11:25 - 12:10.\n🚪 36\n\n5. Физика.\n🕒 12:30 - 13:15.\n🚪 36\n\n6. Алгебра.\n🕒 13:25 - 14:10.\n🚪 36\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 36")

    elif (message.text == 'Среда  7Б'):
        bot.send_message(message.chat.id, "1. Англ. яз.\n🕒 8:30 - 9:15.\n🚪 36 и 22\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 36\n\n3. Обществознание.\n🕒 10:20 - 11:05.\n🚪 36\n\n4. Физ-ра.\n🕒 11:25 - 12:10.\n🚪 Спорт. зал\n\n5. Геометрия.\n🕒 12:30 - 13:15.\n🚪 36\n\n6. Рус. яз.\n🕒 13:25 - 14:10.\n🚪 36")

    elif (message.text == 'Четверг  7Б'):
        bot.send_message(message.chat.id, "1. География.\n🕒 8:30 - 9:15.\n🚪 36\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 36\n\n3. ИЗО.\n🕒 10:20 - 11:05.\n🚪 36\n\n4. Биология.\n🕒 11:25 - 12:10.\n🚪 36\n\n5. Рус. яз.\n🕒 12:30 - 13:15.\n🚪 36\n\n6. Лит-ра.\n🕒 13:25 - 14:10.\n🚪 36")

    elif (message.text == 'Пятница  7Б'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n🚪 Спорт. зал\n\n2. История.\n🕒 9:25 - 10:10.\n🚪 36\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n🚪 36\n\n4. Музыка.\n🕒 11:25 - 12:10.\n🚪 36\n\n5. Физика.\n🕒 12:30 - 13:15.\n🚪 36\n\n6. Тех./Англ.\n🕒 13:25 - 14:10.\n🚪 30 и 36\n\n7. Тех./Англ.\n🕒 14:20 - 15:05.\n🚪 30 и 36")


    #----------------------------------------------7В-----------------------------------------------------------
    elif (message.text == 'Понедельник  7В'):
        bot.send_message(message.chat.id, "1. Рус. яз.\n🕒 8:30 - 9:15.\n🚪 47\n\n2. Музыка.\n🕒 9:25 - 10:10.\n🚪 47\n\n3. История.\n🕒 10:20 - 11:05.\n🚪 47\n\n4. Алгебра.\n🕒 11:25 - 12:10.\n🚪 47\n\n5. Англ. яз.\n🕒 12:30 - 13:15.\n🚪 47 и 30\n\n6. Тех./Фр.\n🕒 13:25 - 14:10.\n🚪 10 и 47\n\n7. Тех./Кит.\n🕒 14:20 - 15:05.\n🚪 10 и 47")

    elif (message.text == 'Вторник  7В'):
        bot.send_message(message.chat.id, "1. Лит-ра.\n🕒 8:30 - 9:15.\n🚪 47\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 47\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n🚪 47\n\n4. Физика.\n🕒 11:25 - 12:10.\n🚪 47\n\n5. ИЗО.\n🕒 12:30 - 13:15.\n🚪 47\n\n6. Англ. яз.\n🕒 13:25 - 14:10.\n🚪 47 и библиотека\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 47")

    elif (message.text == 'Среда  7В'):
        bot.send_message(message.chat.id, "1. География.\n🕒 8:30 - 9:15.\n🚪 47\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n🚪 Спорт. зал\n\n3. Информат.\n🕒 10:20 - 11:05.\n🚪 29 и 31\n\n4. Рус. яз.\n🕒 11:25 - 12:10.\n🚪 47\n\n5. Обществознание.\n🕒 12:30 - 13:15.\n🚪 47\n\n6. Геометрия.\n🕒 13:25 - 14:10.\n🚪 47")

    elif (message.text == 'Четверг  7В'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n🚪 Спорт. зал\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 47\n\n3. География.\n🕒 10:20 - 11:05.\n🚪 47\n\n4. Биология.\n🕒 11:25 - 12:10.\n🚪 47\n\n5. Рус. яз.\n🕒 12:30 - 13:15.\n🚪 47\n\n6. История.\n🕒 13:25 - 14:10.\n🚪 47")

    elif (message.text == 'Пятница  7В'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n🚪 47\n\n2. Лит-ра.\n🕒 9:25 - 10:10.\n🚪 47\n\n3. Физика.\n🕒 10:20 - 11:05.\n🚪 47\n\n4. Англ. яз.\n🕒 11:25 - 12:10.\n🚪 47 и 30\n\n5. Геометрия.\n🕒 12:30 - 13:15.\n🚪 47\n\n6. Тех./Инф.\n🕒 13:25 - 14:10.\n🚪 47 и 31\n\n7. Тех./Инф.\n🕒 14:20 - 15:05.\n🚪 47 и 29\n\n")

    #----------------------------------------------7Г-----------------------------------------------------------
    elif (message.text == 'Понедельник  7Г'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n🚪 24\n\n2. Рус. яз.\n🕒 9:25 - 10:10.\n🚪 24\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n🚪 Спорт. зал\n\n4. Геометрия.\n🕒 11:25 - 12:10.\n🚪 24\n\n5. История.\n🕒 12:30 - 13:15.\n🚪 24\n\n6. Тех./Инф.\n🕒 13:25 - 14:10.\n🚪 24 и 31\n\n7. Тех./Инф.\n🕒 14:20 - 15:05.\n🚪 24 и 29\n\n")

    elif (message.text == 'Вторник  7Г'):
        bot.send_message(message.chat.id, "1. Музыка.\n🕒 8:30 - 9:15.\n🚪 24\n\n2. Биология.\n🕒 9:25 - 10:10.\n🚪 24\n\n3. Обществознание.\n🕒 10:20 - 11:05.\n🚪 24\n\n4. Англ. яз.\n🕒 11:25 - 12:10.\n🚪 24 и библиотека\n\n5. Алгебра.\n🕒 12:30 - 13:15.\n🚪 24\n\n6. Физика.\n🕒 13:25 - 14:10.\n🚪 24")

    elif (message.text == 'Среда  7Г'):
        bot.send_message(message.chat.id, "1. Лит-ра.\n🕒 8:30 - 9:15.\n🚪 24\n\n2. География.\n🕒 9:25 - 10:10.\n🚪 24\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n🚪 24\n\n4. Алгебра.\n🕒 11:25 - 12:10.\n🚪 24\n\n5. Англ. яз.\n🕒 12:30 - 13:15.\n🚪 24 и 33\n\n6. Физ-ра.\n🕒 13:25 - 14:10.\n🚪 Спорт. зал\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 24")

    elif (message.text == 'Четверг  7Г'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n🚪 24\n\n2. История.\n🕒 9:25 - 10:10.\n🚪 24\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n🚪 24\n\n4. ИЗО.\n🕒 11:25 - 12:10.\n🚪 24\n\n5. География.\n🕒 12:30 - 13:15.\n🚪 24\n\n6. Физика.\n🕒 13:25 - 14:10.\n🚪 24")

    elif (message.text == 'Пятница  7Г'):
        bot.send_message(message.chat.id, "1. Физика.\n🕒 8:30 - 9:15.\n🚪 24\n\n2. Рус. яз.\n🕒 9:25 - 10:10.\n🚪 24\n\n3. Англ. яз.\n🕒 10:20 - 11:05.\n🚪 24 и библиотека\n\n4. Геометрия.\n🕒 11:25 - 12:10.\n🚪 24\n\n5. Лит-ра.\n🕒 12:30 - 13:15.\n🚪 24\n\n6. Тех./Кит.\n🕒 13:25 - 14:10.\n🚪 10 и 24\n\n7. Тех./Нем.\n🕒 14:20 - 15:05.\n🚪 10 и 24\n\n")

    #----------------------------------------------7Д-----------------------------------------------------------
    elif (message.text == 'Понедельник  7Д'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n🚪 22\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n🚪 Спорт. зал\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n🚪 22\n\n4. Рус. яз.\n🕒 11:25 - 12:10.\n🚪 22\n\n5. Фр./Кит.\n🕒 12:30 - 13:15.\n🚪 22 и 48\n\n6. Тех./Англ.\n🕒 13:25 - 14:10.\n🚪 42 и 22\n\n7. Тех./Англ.\n🕒 14:20 - 15:05.\n🚪 42 и 22\n\n")

    elif (message.text == 'Вторник  7Д'):
        bot.send_message(message.chat.id, "1. Англ. яз.\n🕒 8:30 - 9:15.\n🚪 22 и 30\n\n2. Геометрия.\n🕒 9:25 - 10:10.\n🚪 22\n\n3. Физика.\n🕒 10:20 - 11:05.\n🚪 22\n\n4. Обществознание.\n🕒 11:25 - 12:10.\n🚪 22\n\n5. Рус. яз.\n🕒 12:30 - 13:15.\n🚪 22\n\n6. Лит-ра.\n🕒 13:25 - 14:10.\n🚪 22\n\n7. Классный час.\n🕒 14:20 - 15:05.\n🚪 22")

    elif (message.text == 'Среда  7Д'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n🚪 Спорт. зал\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 22\n\n3. География.\n🕒 10:20 - 11:05.\n🚪 22\n\n4. ИЗО.\n🕒 11:25 - 12:10.\n🚪 22\n\n5. Рус. яз.\n🕒 12:30 - 13:15.\n🚪 22\n\n6. Геометрия.\n🕒 13:25 - 14:10.\n🚪 22")

    elif (message.text == 'Четверг  7Д'):
        bot.send_message(message.chat.id, "1. Биология.\n🕒 8:30 - 9:15.\n🚪 22\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n🚪 22\n\n3. История.\n🕒 10:20 - 11:05.\n🚪 22\n\n4. Англ. яз.\n🕒 11:25 - 12:10.\n🚪 22 и 30\n\n5. Музыка.\n🕒 12:30 - 13:15.\n🚪 22\n\n6. Лит-ра.\n🕒 13:25 - 14:10.\n🚪 22")

    elif (message.text == 'Пятница  7Д'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n🚪 22\n\n2. География.\n🕒 9:25 - 10:10.\n🚪 22\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n🚪 22\n\n4. Геометрия.\n🕒 11:25 - 12:10.\n🚪 22\n\n5. Физика.\n🕒 12:30 - 13:15.\n🚪 22\n\n6. Тех./Инф.\n🕒 13:25 - 14:10.\n🚪 22 и 29\n\n7. Тех./Инф3.\n🕒 14:20 - 15:05.\n🚪 22 и 31\n\n")\

#----------------------------------------------8А-----------------------------------------------------------
    elif (message.text == 'Понедельник  8А'):
        bot.send_message(message.chat.id, "1. Физика.\n🕒 8:30 - 9:15.\n\n2. Англ. Яз.\n🕒 9:25 - 10:10.\n\n3. Рус. Яз.\n🕒 10:20 - 11:05.\n\n4. Музыка.\n🕒 11:25 - 12:10.\n\n5. История.\n🕒 12:30 - 13.15.\n\n6. География\n🕒 13:25 - 14.10.\n\n7. Алгебра\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Вторник  8А'):
        bot.send_message(message.chat.id, "1. ОБЖ.\n🕒 8:30 - 9:15.\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n\n3. Англ. Яз.\n🕒 10:20 - 11:05.\n\n4. Геометрия.\n🕒 11:25 - 12:10.\n\n5. Биология.\n🕒 12:30 - 13.15.\n\n6. Тех./Фр.\n🕒 13:25 - 14.10.\n\n7. Тех./Кит.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Среда  8А'):
        bot.send_message(message.chat.id, "1. Физика.\n🕒 8:30 - 9:15.\n\n2. Лит-ра.\n🕒 9:25 - 10:10.\n\n3. Обществознаие\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. Алгебра.\n🕒 12:30 - 13.15.\n\n6. Физ-ра\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Четверг  8А'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Геометрия.\n🕒 10:20 - 11:05.\n\n4. Физ-ра.\n🕒 11:25 - 12:10.\n\n5. Биология.\n🕒 12:30 - 13.15.\n\n6. Англ. Яз.\n🕒 13:25 - 14.10.\n\n7. Информатика.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Пятница  8А'):
        bot.send_message(message.chat.id, "1. Химия.\n🕒 8:30 - 9:15.\n\n2. Род. Рус.\n🕒 9:25 - 10:10.\n\n3. Род. Лит.\n🕒 10:20 - 11:05.\n\n4. История.\n🕒 11:25 - 12:10.\n\n5. География.\n🕒 12:30 - 13.15.\n\n6. Физика.\n🕒 13:25 - 14.10.\n")
    #----------------------------------------------8Б-----------------------------------------------------------
    elif (message.text == 'Понедельник  8Б'):
        bot.send_message(message.chat.id, "1. Род. Яз.\n🕒 8:30 - 9:15.\n\n2. География.\n🕒 9:25 - 10:10.\n\n3. Музыка.\n🕒 10:20 - 11:05.\n\n4. Англ. Яз.\n🕒 11:25 - 12:10.\n\n5. Алгебра.\n🕒 12:30 - 13.15.\n\n6. Геометрия.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Вторник  8Б'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Физика.\n🕒 9:25 - 10:10.\n\n3. История.\n🕒 10:20 - 11:05.\n\n4. Биология.\n🕒 11:25 - 12:10.\n\n5. Англ. Яз.\n🕒 12:30 - 13.15.\n\n6. Тех./Кит.\n🕒 13:25 - 14.10.\n\n7. Тех./Фр.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Среда  8Б'):
        bot.send_message(message.chat.id, "1. Физика.\n🕒 8:30 - 9:15.\n\n2. Информатика.\n🕒 9:25 - 10:10.\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. Рус. яз.\n🕒 12:30 - 13.15.\n\n6. Лит-ра.\n🕒 13:25 - 14.10.\n\n7. Геометрия.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Четверг  8Б'):
        bot.send_message(message.chat.id, "1. ОБЖ.\n🕒 8:30 - 9:15.\n\n2. Обществознание.\n🕒 9:25 - 10:10.\n\n3. История.\n🕒 10:20 - 11:05.\n\n4. Алгебра.\n🕒 11:25 - 12:10.\n\n5. Физика.\n🕒 12:30 - 13.15.\n\n6. Физ-ра.\n🕒 13:25 - 14.10.\n\n7. Англ. Яз\n🕒 14:20 - 15:05..")

    elif (message.text == 'Пятница  8Б'):
        bot.send_message(message.chat.id, "1. Биология.\n🕒 8:30 - 9:15.\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n\n3. Химия.\n🕒 10:20 - 11:05.\n\n4. География.\n🕒 11:25 - 12:10.\n\n5. Рус. Яз.\n🕒 12:30 - 13.15.\n\n6. Род. Лит.\n🕒 13:25 - 14.10.\n\n7. Класс. Час.\n🕒 14:20 - 15:05.")

#----------------------------------------------8В-----------------------------------------------------------
    elif (message.text == 'Понедельник  8В'):
        bot.send_message(message.chat.id, "1. География.\n🕒 8:30 - 9:15.\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n\n3. Англ. Яз.\n🕒 10:20 - 11:05.\n\n4. Физ-ра.\n🕒 11:25 - 12:10.\n\n5. Биология.\n🕒 12:30 - 13.15.\n\n6. Музыка.\n🕒 13:25 - 14.10.\n\n7. Физика.")

    elif (message.text == 'Вторник  8В'):
        bot.send_message(message.chat.id, "1. Геометрия.\n🕒 8:30 - 9:15.\n\n2. Обществознание.\n🕒 9:25 - 10:10.\n\n3. Химия.\n🕒 10:20 - 11:05.\n\n4. Информатика.\n🕒 11:25 - 12:10.\n\n5. Рус. Яз.\n🕒 12:30 - 13.15.\n\n6. Тех./Англ.\n🕒 13:25 - 14.10.\n\n7. Тех./Англ.")

    elif (message.text == 'Среда  8В'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Биология.\n🕒 10:20 - 11:05.\n\n4. История.\n🕒 11:25 - 12:10.\n\n5. Физика.\n🕒 12:30 - 13.15.\n\n6. ОБЖ.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Четверг  8В'):
        bot.send_message(message.chat.id, "1. Информатика.\n🕒 8:30 - 9:15.\n\n2. Род. Яз.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. Физ-ра.\n🕒 12:30 - 13.15.\n\n6. Лит-ра.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Пятница  8В'):
        bot.send_message(message.chat.id, "1. География.\n🕒 8:30 - 9:15.\n\n2. Англ. Яз.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. Кит./Фр.\n🕒 11:25 - 12:10.\n\n5. Геометрия.\n🕒 12:30 - 13.15.\n\n6. История.\n🕒 13:25 - 14.10.\n\n7. Род. Лит.")
#----------------------------------------------8Г-----------------------------------------------------------
    elif (message.text == 'Понедельник  8Г'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Экономика.\n🕒 10:20 - 11:05.\n\n4. Биология.\n🕒 11:25 - 12:10.\n\n5. Англ. Яз.\n🕒 12:30 - 13.15.\n\n6. Родной язык.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Вторник  8Г'):
        bot.send_message(message.chat.id, "1. География.\n🕒 8:30 - 9:15.\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. Геометрия.\n🕒 12:30 - 13.15.\n\n6. Тех./Англ.\n🕒 13:25 - 14.10.\n\n7. Тех./Англ.")

    elif (message.text == 'Среда  8Г'):
        bot.send_message(message.chat.id, "1. Биология.\n🕒 8:30 - 9:15.\n\n2. Химия.\n🕒 9:25 - 10:10.\n\n3. Физика.\n🕒 10:20 - 11:05.\n\n4. Обществознание.\n🕒 11:25 - 12:10.\n\n5. Лит-ра.\n🕒 12:30 - 13.15.\n\n6. История.\n🕒 13:25 - 14.10.\n\n7. ОБЖ.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Четверг  8Г'):
        bot.send_message(message.chat.id, "1. Рус. Яз.\n🕒 8:30 - 9:15.\n\n2. Информатика.\n🕒 9:25 - 10:10.\n\n3. Физика.\n🕒 10:20 - 11:05.\n\n4. Алгебра.\n🕒 11:25 - 12:10.\n\n5. Геометрия.\n🕒 12:30 - 13.15.\n\n6. География.\n🕒 13:25 - 14.10.\n\n7. Физ-ра.")

    elif (message.text == 'Пятница  8Г'):
        bot.send_message(message.chat.id, "1. Англ. Яз.\n🕒 8:30 - 9:15.\n\n2. История.\n🕒 9:25 - 10:10.\n\n3. Кит./Фр.\n🕒 10:20 - 11:05.\n\n4. Род. Лит.\n🕒 11:25 - 12:10.\n\n5. Музыка.\n🕒 12:30 - 13.15.\n\n6. Алгебра.\n🕒 13:25 - 14.10.\n")

#----------------------------------------------9А-----------------------------------------------------------
    elif (message.text == 'Понедельник  9А'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Физика.\n🕒 9:25 - 10:10.\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. География.\n🕒 12:30 - 13.15.\n\n6. Англ. Яз.\n🕒 13:25 - 14.10.\n\n7. Геометрия.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Вторник  9А'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n\n4. Родной язык.\n🕒 11:25 - 12:10.\n\n5. Алгебра.\n🕒 12:30 - 13.15.\n\n6. Алгебра.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Среда  9А'):
        bot.send_message(message.chat.id, "1. Физика.\n🕒 8:30 - 9:15.\n\n2. Биология.\n🕒 9:25 - 10:10.\n\n3. География.\n🕒 10:20 - 11:05.\n\n4. Лит-ра.\n🕒 11:25 - 12:10.\n\n5. Геометрия.\n🕒 12:30 - 13.15.\n\n6. Технология.\n🕒 13:25 - 14.10.\n\n7. Классный час.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Четверг  9А'):
        bot.send_message(message.chat.id, "1. Англ. Яз.\n🕒 8:30 - 9:15.\n\n2. Химия.\n🕒 9:25 - 10:10.\n\n3. Информатика.\n🕒 10:20 - 11:05.\n\n4. Родная литература.\n🕒 11:25 - 12:10.\n\n5. Обществознание.\n🕒 12:30 - 13.15.\n\n6. ОБЖ.\n🕒 13:25 - 14.10.\n\n7. Физика.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Пятница  9А'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Биология.\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. Англ. Яз.\n🕒 12:30 - 13.15.\n\n6. Алгебра.\n🕒 13:25 - 14.10.\n\n7. Физ-ра.\n🕒 14:20 - 15:05.\n\n")
#----------------------------------------------9Б-----------------------------------------------------------

    elif (message.text == 'Понедельник  9Б'):
        bot.send_message(message.chat.id, "1. Лит-ра.\n🕒 8:30 - 9:15.\n\n2. Англ. Яз.\n🕒 9:25 - 10:10.\n\n3. Рус. яз.\n🕒 10:20 - 11:05.\n\n4. Информатика.\n🕒 11:25 - 12:10.\n\n5. Алгебра.\n🕒 12:30 - 13.15.\n\n6. Геометрия.\n🕒 13:25 - 14.10.\n\n7. Физика.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Вторник  9Б'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. История.\n🕒 9:25 - 10:10.\n\n3. Химия.\n🕒 10:20 - 11:05.\n\n4. География.\n🕒 11:25 - 12:10.\n\n5. Геометрия.\n🕒 12:30 - 13.15.\n\n6. ОБЖ.\n🕒 13:25 - 14.10.\n\n7. Физ-ра.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Среда  9Б'):
        bot.send_message(message.chat.id, "1. Биология.\n🕒 8:30 - 9:15.\n\n2. Физика.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. Родной язык.\n🕒 11:25 - 12:10.\n\n5. Геометрия.\n🕒 12:30 - 13.15.\n\n6. Тех./Англ.\n🕒 13:25 - 14.10.\n\n7. Тех./Англ.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Четверг  9Б'):
        bot.send_message(message.chat.id, "1. Физ-ра.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Родная литература.\n🕒 10:20 - 11:05.\n\n4. Обществознание.\n🕒 11:25 - 12:10.\n\n5. Англ. Яз.\n🕒 12:30 - 13.15.\n\n6. Физика.\n🕒 13:25 - 14.10.\n\n7. Классный час.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Пятница  9Б'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Биология.\n🕒 9:25 - 10:10.\n\n3. История.\n🕒 10:20 - 11:05.\n\n4. Рус. Яз\n🕒 11:25 - 12:10.\n\n5. Химия.\n🕒 12:30 - 13.15.\n\n6. География.\n🕒 13:25 - 14.10.\n")
#----------------------------------------------9В-----------------------------------------------------------
    elif (message.text == 'Понедельник  9В'):
        bot.send_message(message.chat.id, "1. Англ. Яз.\n🕒 8:30 - 9:15.\n\n2. Информатика.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. География.\n🕒 11:25 - 12:10.\n\n5. История.\n🕒 12:30 - 13.15.\n\n6. Физика.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Вторник  9В'):
        bot.send_message(message.chat.id, "1. Лит-ра.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. ОбЖ.\n🕒 12:30 - 13.15.\n\n6. Биология.\n🕒 13:25 - 14.10.\n\n7. Геометрия.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Среда  9В'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n\n3. Родной язык.\n🕒 10:20 - 11:05.\n\n4. Физика.\n🕒 11:25 - 12:10.\n\n5. Информатика.\n🕒 12:30 - 13.15.\n\n6. Тех./Англ.\n🕒 13:25 - 14.10.\n\n7. Тех./Англ.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Четверг  9В'):
        bot.send_message(message.chat.id, "1. Рус. Яз.\n🕒 8:30 - 9:15.\n\n2. География.\n🕒 9:25 - 10:10.\n\n3. Химия.\n🕒 10:20 - 11:05.\n\n4. Англ. Яз.\n🕒 11:25 - 12:10.\n\n5. Физика.\n🕒 12:30 - 13.15.\n\n6. Обществознание.\n🕒 13:25 - 14.10.\n\n7. Физ-ра.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Пятница  9В'):
        bot.send_message(message.chat.id, "1. Родная литература.\n🕒 8:30 - 9:15.\n\n2. История.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. Геометрия.\n🕒 11:25 - 12:10.\n\n5. Рус. Яз.\n🕒 12:30 - 13.15.\n\n6. Биология.\n🕒 13:25 - 14.10.\n\n7. Классный час.\n🕒 14:20 - 15:05.")

#----------------------------------------------9Г-----------------------------------------------------------
    elif (message.text == 'Понедельник  9Г'):
        bot.send_message(message.chat.id, "1. Физика.\n🕒 8:30 - 9:15.\n\n2. Химия.\n🕒 9:25 - 10:10.\n\n3. Англ. Яз.\n🕒 10:20 - 11:05.\n\n4. физика.\n🕒 11:25 - 12:10.\n\n5. Рус. Яз.\n🕒 12:30 - 13.15.\n\n6. Лит-ра.\n🕒 13:25 - 14.10.\n\n7. Классный час.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Вторник  9Г'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. География.\n🕒 9:25 - 10:10.\n\n3. История.\n🕒 10:20 - 11:05.\n\n4. Биология.\n🕒 11:25 - 12:10.\n\n5. Химия.\n🕒 12:30 - 13.15.\n\n6. Геометрия.\n🕒 13:25 - 14.10.\n\n7. Физ-ра.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Среда  9Г'):
        bot.send_message(message.chat.id, "1. Родная литература.\n🕒 8:30 - 9:15.\n\n2. Родной язык.\n🕒 9:25 - 10:10.\n\n3. Физика.\n🕒 10:20 - 11:05.\n\n4. Алгебра.\n🕒 11:25 - 12:10.\n\n5. Англ. Яз.\n🕒 12:30 - 13.15.\n\n6. Тех./Инф.\n🕒 13:25 - 14.10.\n\n7. Тех./Инф.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Четверг  9Г'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Физика.\n🕒 9:25 - 10:10.\n\n3. Англ. Яз.\n🕒 10:20 - 11:05.\n\n4. Рус. Яз.\n🕒 11:25 - 12:10.\n\n5. Обществознание.\n🕒 12:30 - 13.15.\n\n6. Геометрия.\n🕒 13:25 - 14.10.\n\n7. ОБЖ.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Пятница  9Г'):
        bot.send_message(message.chat.id, "1. Биология.\n🕒 8:30 - 9:15.\n\n2. Алгебра.\n🕒 9:25 - 10:10.\n\n3. География.\n🕒 10:20 - 11:05.\n\n4. Физ-ра.\n🕒 11:25 - 12:10.\n\n5. История.\n🕒 12:30 - 13.15.\n\n6. Рус. Яз.\n🕒 13:25 - 14.10.\n")
    #----------------------------------------------9Д-----------------------------------------------------------
    elif (message.text == 'Понедельник  9Д'):
        bot.send_message(message.chat.id, "1. Химия.\n🕒 8:30 - 9:15.\n\n2. География.\n🕒 9:25 - 10:10.\n\n3. Рус. Яз.\n🕒 10:20 - 11:05.\n\n4. Англ. Яз.\n🕒 11:25 - 12:10.\n\n5. Физика.\n🕒 12:30 - 13.15.\n\n6. История.\n🕒 13:25 - 14.10.\n\n7. Физ-ра.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Вторник  9Д'):
        bot.send_message(message.chat.id, "1. Обществознание.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. Лит-ра.\n🕒 11:25 - 12:10.\n\n5. Геометрия.\n🕒 12:30 - 13.15.\n\n6. Биология.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Среда  9Д'):
        bot.send_message(message.chat.id, "1. Алгебра.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n\n4. Англ. Яз.\n🕒 11:25 - 12:10.\n\n5. Физика.\n🕒 12:30 - 13.15.\n\n6. Тех./Инф.\n🕒 13:25 - 14.10.\n\n7. Тех./Инф.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Четверг  9Д'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n\n2. Англ. Яз.\n🕒 9:25 - 10:10.\n\n3. Алгебра.\n🕒 10:20 - 11:05.\n\n4. Физика.\n🕒 11:25 - 12:10.\n\n5. ОБЖ.\n🕒 12:30 - 13.15.\n\n6. География.\n🕒 13:25 - 14.10.\n\n7. Геометрия.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Пятница  9Д'):
        bot.send_message(message.chat.id, "1. Химия.\n🕒 8:30 - 9:15.\n\n2. Родной язык.\n🕒 9:25 - 10:10.\n\n3. Родная литература.\n🕒 10:20 - 11:05.\n\n4. Биология.\n🕒 11:25 - 12:10.\n\n5. Алгебра.\n🕒 12:30 - 13.15.\n\n6. Геометрия.\n🕒 13:25 - 14.10.\n")
    
     #----------------------------------------------10А-----------------------------------------------------------
    elif (message.text == 'Понедельник  10А'):
        bot.send_message(message.chat.id, "1. Англ. Яз.\n🕒 8:30 - 9:15.\n\n2. Рус. Яз.\n🕒 9:25 - 10:10.\n\n3. Лит-ра.\n🕒 10:20 - 11:05.\n\n4. История.\n🕒 11:25 - 12:10.\n\n5. Астрономия.\n🕒 12:30 - 13.15.\n\n6. Матем./Матем.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Вторник  10А'):
        bot.send_message(message.chat.id, "1. Родной язык.\n🕒 8:30 - 9:15.\n\n2. ОбЖ.\n🕒 9:25 - 10:10.\n\n3. Физика.\n🕒 10:20 - 11:05.\n\n4. Матем./Матем.\n🕒 11:25 - 12:10.\n\n5. Физ-ра.\n🕒 12:30 - 13.15.\n\n6. Хим./Хим.\n🕒 13:25 - 14.10.\n\n7. Матем./Био.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Среда  10А'):
        bot.send_message(message.chat.id, "1. Экон./Хим.\n🕒 8:30 - 9:15.\n\n2. Англ. Яз.\n🕒 9:25 - 10:10.\n\n3. Рус. Яз.\n🕒 10:20 - 11:05.\n\n4. Лит-ра.\n🕒 11:25 - 12:10.\n\n5. Матем./Матем.\n🕒 12:30 - 13.15.\n\n6. Матем./Матем.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Четверг  10А'):
        bot.send_message(message.chat.id, "1. Обществознание.\n🕒 8:30 - 9:15.\n\n2. Биол./Биол.\n🕒 9:25 - 10:10.\n\n3. Матем./Биол.\n🕒 10:20 - 11:05.\n\n4. Физика.\n🕒 11:25 - 12:10.\n\n5. Информатика.\n🕒 12:30 - 13.15.\n\n6. Хим./Экон.\n🕒 13:25 - 14.10.\n\n7. Классный час.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Пятница  10А'):
        bot.send_message(message.chat.id, "1. Матем./Матем.\n🕒 8:30 - 9:15.\n\n2. Лит-ра.\n🕒 9:25 - 10:10.\n\n3. История.\n🕒 10:20 - 11:05.\n\n4. География.\n🕒 11:25 - 12:10.\n\n5. Англ. яз.\n🕒 12:30 - 13.15.\n\n6. Физ-ра.\n🕒 13:25 - 14.10.\n")

     #----------------------------------------------10Б-----------------------------------------------------------
    elif (message.text == 'Понедельник  10Б'):
        bot.send_message(message.chat.id, "1. Инф./Инф.\n🕒 8:30 - 9:15.\n\n2. Астрономия.\n🕒 9:25 - 10:10.\n\n3. Физ./Физ.\n🕒 10:20 - 11:05.\n\n4. Матем.\n🕒 11:25 - 12:10.\n\n5. Матем.\n🕒 12:30 - 13.15.\n\n6. Англ. яз.\n🕒 13:25 - 14.10.\n\n7. Програм./\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Вторник  10Б'):
        bot.send_message(message.chat.id, "1. Физика.\n🕒 8:30 - 9:15.\n\n2. Матем.\n🕒 9:25 - 10:10.\n\n3. Рус./Род.\n🕒 10:20 - 11:05.\n\n4. Лит-ра.\n🕒 11:25 - 12:10.\n\n5. Химия.\n🕒 12:30 - 13.15.\n\n6. Физ-ра.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Среда  10Б'):
        bot.send_message(message.chat.id, "1. Инф./Инф.\n🕒 8:30 - 9:15.\n\n2. Матем.\n🕒 9:25 - 10:10.\n\n3. Англ. яз.\n🕒 10:20 - 11:05.\n\n4. ОБЖ.\n🕒 11:25 - 12:10.\n\n5. История.\n🕒 12:30 - 13.15.\n\n6. Физика./\n🕒 13:25 - 14.10.\n\n7. Физика./\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Четверг  10Б'):
        bot.send_message(message.chat.id, "1. Физ./Физ.\n🕒 8:30 - 9:15.\n\n2. Матем.\n🕒 9:25 - 10:10.\n\n3. Биология.\n🕒 10:20 - 11:05.\n\n4. Обществознание.\n🕒 11:25 - 12:10.\n\n5. Лит-ра.\n🕒 12:30 - 13.15.\n\n6. Инф./Инф.\n🕒 13:25 - 14.10.\n\n7. Матем.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Пятница  10Б'):
        bot.send_message(message.chat.id, "1. История.\n🕒 8:30 - 9:15.\n\n2. Лит-ра.\n🕒 9:25 - 10:10.\n\n3. География.\n🕒 10:20 - 11:05.\n\n4. Англ. яз\n🕒 11:25 - 12:10.\n\n5. Физ-ра.\n🕒 12:30 - 13.15.\n\n6. Матем.\n🕒 13:25 - 14.10.\n\n7. Классный час\n🕒 14:20 - 15:05.\n\n")

      #----------------------------------------------11А-----------------------------------------------------------
    elif (message.text == 'Понедельник  11А'):
        bot.send_message(message.chat.id, "1. Матем.\n🕒 8:30 - 9:15.\n\n2. Матем.\n🕒 9:25 - 10:10.\n\n3. История.\n🕒 10:20 - 11:05.\n\n4. Рус./Род.\n🕒 11:25 - 12:10.\n\n5. Лит-ра.\n🕒 12:30 - 13.15.\n\n6. Физ-ра.\n🕒 13:25 - 14.10.\n\n7. Биология.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Вторник  11А'):
        bot.send_message(message.chat.id, "1. нет.\n\n2. Лит-ра.\n🕒 9:25 - 10:10.\n\n3. География.\n🕒 10:20 - 11:05.\n\n4. Матем.\n🕒 11:25 - 12:10.\n\n5. Англ. яз.\n🕒 12:30 - 13.15.\n\n6. Информатика.\n🕒 13:25 - 14.10.\n\n7. Физика.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Среда  11А'):
        bot.send_message(message.chat.id, "1. ОБЖ.\n🕒 8:30 - 9:15.\n\n2. Англ. яз.\n🕒 9:25 - 10:10.\n\n3. Матем.\n🕒 10:20 - 11:05.\n\n4. Химия.\n🕒 11:25 - 12:10.\n\n5. Обществознание.\n🕒 12:30 - 13.15.\n\n6. Эконом./Хим.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Четверг  11А'):
        bot.send_message(message.chat.id, "1. Экон./Хим.\n🕒 8:30 - 9:15.\n\n2. Биология.\n🕒 9:25 - 10:10.\n\n3. Физ-ра.\n🕒 10:20 - 11:05.\n\n4. Матем.\n🕒 11:25 - 12:10.\n\n5. Матем.\n🕒 12:30 - 13.15.\n\n6. Лит-ра.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Пятница  11А'):
        bot.send_message(message.chat.id, "1. Информатика.\n🕒 8:30 - 9:15.\n\n2. Физика.\n🕒 9:25 - 10:10.\n\n3. Матем.\n🕒 10:20 - 11:05.\n\n4. История.\n🕒 11:25 - 12:10.\n\n5. Англ. яз.\n🕒 12:30 - 13.15.\n\n6. Общ./Био.\n🕒 13:25 - 14.10.\n\n7. Классный час\n🕒 14:20 - 15:05.\n\n")
    
     #----------------------------------------------11Б-----------------------------------------------------------
    elif (message.text == 'Понедельник  11Б'):
        bot.send_message(message.chat.id, "1. Матем.\n🕒 8:30 - 9:15.\n\n2. История.\n🕒 9:25 - 10:10.\n\n3. Информатика.\n🕒 10:20 - 11:05.\n\n4. Лит-ра.\n🕒 11:25 - 12:10.\n\n5. Физ-ра.\n🕒 12:30 - 13.15.\n\n6. Физика.\n🕒 13:25 - 14.10.\n")

    elif (message.text == 'Вторник  11Б'): 
        bot.send_message(message.chat.id, "1. Матем.\n🕒 8:30 - 9:15.\n\n2. География.\n🕒 9:25 - 10:10.\n\n3. Матем.\n🕒 10:20 - 11:05.\n\n4. Англ. яз.\n🕒 11:25 - 12:10.\n\n5. Информатика.\n🕒 12:30 - 13.15.\n\n6. Лит-ра.\n🕒 13:25 - 14.10.\n\n7. Классный час.\n🕒 14:20 - 15:05.")

    elif (message.text == 'Среда  11Б'):
        bot.send_message(message.chat.id, "1. нет.\n\n2. ОБЖ.\n🕒 9:25 - 10:10.\n\n3. Обществознание.\n🕒 10:20 - 11:05.\n\n4. Англ. яз.\n🕒 11:25 - 12:10.\n\n5. Химия.\n🕒 12:30 - 13.15.\n\n6. Физика\n🕒 13:25 - 14.10.\n\n7. Матем.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Четверг  11Б'):
        bot.send_message(message.chat.id, "1. Биология.\n🕒 8:30 - 9:15.\n\n2. Физ-ра.\n🕒 9:25 - 10:10.\n\n3. История.\n🕒 10:20 - 11:05.\n\n4. Рус. яз.\n🕒 11:25 - 12:10.\n\n5. Лит-ра.\n🕒 12:30 - 13.15.\n\n6. Матем.\n🕒 13:25 - 14.10.\n\n7. Физика.\n🕒 14:20 - 15:05.\n\n")

    elif (message.text == 'Пятница  11Б'):
        bot.send_message(message.chat.id, "1. нет.\n🕒 8:30 - 9:15.\n\n2. Информатика.\n🕒 9:25 - 10:10.\n\n3. Програм.\n🕒 10:20 - 11:05.\n\n4. Матем.\n🕒 11:25 - 12:10.\n\n5. Матем.\n🕒 12:30 - 13.15.\n\n6. Англ. яз.\n🕒 13:25 - 14.10.\n\n7. Физика.\n🕒 14:20 - 15:05.\n\n")

    else:
          bot.send_message(message.chat.id, "Я вас не понимаю. Для повторного запуска бота напишите /start")












bot.polling(none_stop=True)





