import telebot
from telebot import types

bot = telebot.TeleBot('1637177992:AAHdwLXzWKcTJYivYXHzGUc3iQcx5Xf7olA')


#  Приветствие
@bot.message_handler(commands=['start'])
def welcome(message):
    #  стикер при первом запуске бота
    sti = open('static/start.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("К началу ↑")
    markup.add(item0)

    #  приветствие
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!\nЯ\
- <b>{1.first_name}</b>, бот созданный чтобы помочь Вам в выборе косметологической процедуры."
                     .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

    #  создание кнопок под сообщением
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Морщины', callback_data='Morshini'),
        telebot.types.InlineKeyboardButton('Акне', callback_data='Akne'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Выпадение волос', callback_data='Vipadenie'),
        telebot.types.InlineKeyboardButton('Пигментация', callback_data='Pigmentacia'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Постакне', callback_data='Postakne'),
        telebot.types.InlineKeyboardButton('Второй подбородок', callback_data='Vtoroy_podborodok'))
    bot.send_message(message.chat.id, 'Какая проблема Вас беспокоит?', reply_markup=keyboard)


#  Приветствие при нажатии кнопки "К началу ↑"
@bot.message_handler(commands=['text'])
def welcome_new(message):
    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("К началу ↑")
    markup.add(item0)

    #  приветствие
    bot.send_message(message.chat.id, "Здравствуйте ещё раз, {0.first_name}!"
                     .format(message.from_user), parse_mode='html', reply_markup=markup)

    #  создание кнопок под сообщением
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Морщины', callback_data='Morshini'),
        telebot.types.InlineKeyboardButton('Акне', callback_data='Akne'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Выпадение волос', callback_data='Vipadenie'),
        telebot.types.InlineKeyboardButton('Пигментация', callback_data='Pigmentacia'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Постакне', callback_data='Postakne'),
        telebot.types.InlineKeyboardButton('Второй подбородок', callback_data='Vtoroy_podborodok'))
    bot.send_message(message.chat.id, 'Какая проблема Вас беспокоит?', reply_markup=keyboard)


#  Основное дерево бота
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    try:
        if call.message:
            # МОРЩИНЫ: 1.Лоб, 2.Вокруг глаз, 3.Носогубные, 4.Вокруг губ.
            if call.data == 'Morshini':
                morshini(call)
            # 1.Лоб.
            elif call.data == 'Lob':
                lob(call)
            elif call.data == 'Botox':
                botox(call)
            elif call.data == 'Botox_info':
                botox_info(call)
            elif call.data == 'Biorevit':
                biorevit(call)
            elif call.data == 'Biorevit_info':
                biorevit_info(call)
            elif call.data == 'Filler':
                filler(call)
            elif call.data == 'Filler_info':
                filler_info(call)
            # 2.Вокруг глаз.
            elif call.data == 'Vokrug_glaz':
                vokrug_glaz(call)
            elif call.data == 'Botox_other':
                botox_other(call)
            elif call.data == 'Botox_info':
                botox_info(call)
            elif call.data == 'Biorevit_other':
                biorevit_other(call)
            elif call.data == 'Biorevit_info':
                biorevit_info(call)
            # 3.Носогубные.
            elif call.data == 'Nosogubnie':
                nosogubnie(call)
            elif call.data == 'Filler':
                filler(call)
            elif call.data == 'Lipolitiki':
                lipolitiki(call)
            elif call.data == 'Lipolitiki_info':
                lipolitiki_info(call)
            # 4.Вокруг губ.
            elif call.data == 'Vokrug_gub':
                vokrug_gub(call)
            elif call.data == 'Filler':
                filler(call)

            # АКНЕ
            elif call.data == 'Akne':
                akne(call)
            elif call.data == 'Piling':
                piling(call)
            elif call.data == 'Poverhnostniy':
                poverhnostniy(call)
            elif call.data == 'Poverhnostniy_info':
                poverhnostniy_info(call)
            elif call.data == 'Sredinniy':
                sredinniy(call)
            elif call.data == 'Sredinniy_info':
                sredinniy_info(call)
            elif call.data == 'Chistka_lica':
                chistka_lica(call)
            elif call.data == 'Chistka_lica_info':
                chistka_lica_info(call)
            elif call.data == 'Mezoterapia':
                mezoterapia(call)
            elif call.data == 'Mezoterapia_info':
                mezoterapia_info(call)

            # ВЫПАДЕНИЕ ВОЛОС
            elif call.data == 'Vipadenie':
                vipadenie(call)
            elif call.data == 'Mezoterapia_dermaheal':
                mezoterapia_dermaheal(call)
            elif call.data == 'Mezoterapia_dermaheal_info':
                mezoterapia_dermaheal_info(call)

            # ПИГМЕНТАЦИЯ
            elif call.data == 'Pigmentacia':
                pigmentacia(call)
            elif call.data == 'Piling_pigment': # Piling_1
                piling_pigment(call)
            elif call.data == 'Poverhnostniy_pigment': # Poverhnostniy_1
                poverhnostniy_pigment(call)
            elif call.data == 'Poverhnostniy_pigment_info': # Poverhnostniy_1_info
                poverhnostniy_pigment_info(call)
            elif call.data == 'Sredinniy':
                sredinniy(call)
            elif call.data == 'Mezoterapia_pigment': # Mezoterapia_1
                mezoterapia_pigment(call)
            elif call.data == 'Mezoterapia_pigment_info': # Mezoterapia_2_info
                mezoterapia_pigment_info(call)

            # ПОСТАКНЕ
            elif call.data == 'Postakne':
                postakne(call)
            elif call.data == 'Piling_pigment': # Piling_1
                piling_pigment(call)
            elif call.data == 'Mezoterapia_pigment': # Mezoterapia_2
                mezoterapia_pigment(call)
            elif call.data == 'Carboxi':
                carboxi(call)
            elif call.data == 'Carboxi_info':
                carboxi_info(call)

            # ВТОРОЙ ПОДБОРОДОК
            elif call.data == 'Vtoroy_podborodok':
                vtoroy_podborodok(call)
            elif call.data == 'Lipolitiki':
                lipolitiki(call)

    except Exception as e:
        print(repr(e))


# МОРЩИНЫ
def morshini(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Морщины"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Лоб", callback_data='Lob')
    item2 = types.InlineKeyboardButton("Вокруг глаз", callback_data='Vokrug_glaz')
    item3 = types.InlineKeyboardButton("Носогубные", callback_data='Nosogubnie')
    item4 = types.InlineKeyboardButton("Вокруг губ", callback_data='Vokrug_gub')

    markup.add(item1, item2, item3, item4)

    bot.send_message(call.message.chat.id, '*Морщины где?*', reply_markup=markup, parse_mode="Markdown")


def lob(call):
    pass


def botox(call):
    pass


def botox_info(call):
    pass


def biorevit(call):
    pass


def biorevit_info(call):
    pass


def filler(call):
    pass


def filler_info(call):
    pass


def vokrug_glaz(call):
    pass


def botox_other(call):
    pass


def botox_info(call):
    pass


def biorevit_other(call):
    pass


def biorevit_info(call):
    pass


def nosogubnie(call):
    pass


def filler(call):
    pass


def lipolitiki(call):
    pass


def lipolitiki_info(call):
    pass

def vokrug_gub(call):
    pass


# АКНЕ
def akne(call):
    pass


def piling(call):
    pass


def poverhnostniy(call):
    pass


def poverhnostniy_info(call):
    pass


def sredinniy(call):
    pass


def sredinniy_info(call):
    pass


def chistka_lica(call):
    pass


def chistka_lica_info(call):
    pass


def mezoterapia(call):
    pass


def mezoterapia_info(call):
    pass


# ВЫПАДЕНИЕ ВОЛОС
def vipadenie(call):
    pass


def mezoterapia_dermaheal(call):
    pass


def mezoterapia_dermaheal_info(call):
    pass


# ПИГМЕНТАЦИЯ
def pigmentacia(call):
    pass


def piling_pigment(call):
    pass


def poverhnostniy_pigment(call):
    pass


def poverhnostniy_pigment_info(call):
    pass


def mezoterapia_pigment(call):
    pass


def mezoterapia_pigment_info(call):
    pass


# ПОСТАКНЕ
def postakne(call):
    pass


def carboxi(call):
    pass


def carboxi_info(call):
    pass


# ВТОРОЙ ПОДБОРОДОК
def vtoroy_podborodok(call):
    pass



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'К началу ↑':
            welcome_new(message)
        else:
            bot.send_message(message.chat.id, 'Выберите один вариант из предложенных выше, пожалуйста.')


# RUN
bot.polling(none_stop=True)