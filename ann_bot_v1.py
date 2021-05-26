import telebot
from telebot import types

bot = telebot.TeleBot('1637177992:AAF0EK96jgeBS95Mj04BxV8nP4GWJKonyZ0')


#  Приветствие
@bot.message_handler(commands=['start'])
def welcome(message):
    #  стикер при первом запуске бота
    sti = open('static/start.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("К началу ↑")
    item00 = types.KeyboardButton("☎ Записаться на процедуру")
    markup.add(item0, item00)

    # приветствие
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы "
                                      "помочь Вам в выборе косметологической процедуры."
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
        telebot.types.InlineKeyboardButton('Жировые отложения', callback_data='Zhirovie_otlozheniya'))

    # сообщение
    bot.send_message(message.chat.id, 'Какая проблема Вас беспокоит?', reply_markup=keyboard)


#  Приветствие при нажатии кнопки "К началу ↑"
@bot.message_handler(commands=['text'])
def welcome_new(message):
    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton("К началу ↑")
    item00 = types.KeyboardButton("☎ Записаться на процедуру")
    markup.add(item0, item00)

    # приветствие
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
        telebot.types.InlineKeyboardButton('Жировые отложения', callback_data='Zhirovie_otlozheniya'))
    # сообщение
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
            elif call.data == 'Filler_info':
                filler_info(call)
            # 4.Вокруг губ.
            elif call.data == 'Vokrug_gub':
                vokrug_gub(call)
            elif call.data == 'Filler':
                filler(call)
            # 5.Лица и шеи
            elif call.data == 'Lica_i_shei':
                lica_i_shei(call)
            elif call.data == 'Biorevit':
                biorevit(call)

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
            elif call.data == 'Piling_pigment':  # Piling_1
                piling_pigment(call)
            elif call.data == 'Poverhnostniy_pigment':  # Poverhnostniy_1
                poverhnostniy_pigment(call)
            elif call.data == 'Poverhnostniy_pigment_info':  # Poverhnostniy_1_info
                poverhnostniy_pigment_info(call)
            elif call.data == 'Sredinniy':
                sredinniy(call)
            elif call.data == 'Mezoterapia_pigment':  # Mezoterapia_1
                mezoterapia_pigment(call)
            elif call.data == 'Mezoterapia_pigment_info':  # Mezoterapia_2_info
                mezoterapia_pigment_info(call)

            # ПОСТАКНЕ
            elif call.data == 'Postakne':
                postakne(call)
            elif call.data == 'Piling_pigment':  # Piling_1
                piling_pigment(call)
            elif call.data == 'Mezoterapia_pigment':  # Mezoterapia_2
                mezoterapia_pigment(call)
            elif call.data == 'Carboxi':
                carboxi(call)
            elif call.data == 'Carboxi_info':
                carboxi_info(call)

            # ЖИРОВЫЕ ОТЛОЖЕНИЯ
            elif call.data == 'Zhirovie_otlozheniya':
                zhirovie_otlozheniya(call)
            elif call.data == 'Lipolitiki_zhir':
                lipolitiki_zhir(call)
            elif call.data == 'Lipolitiki_zhir_info':
                lipolitiki_zhir_info(call)

    except Exception as e:
        print(repr(e))


# Запись
def my_info(message):
    bot.send_message(message.chat.id, '📞 +79534219598\n➡ Instagram.com/anna_igolkina71')


# МОРЩИНЫ
def morshini(call):
    # Картинка
    photo = open('static/morshini.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Лоб", callback_data='Lob')
    item2 = types.InlineKeyboardButton("Вокруг глаз", callback_data='Vokrug_glaz')
    item3 = types.InlineKeyboardButton("Носогубные", callback_data='Nosogubnie')
    item4 = types.InlineKeyboardButton("Вокруг губ", callback_data='Vokrug_gub')
    item42 = types.InlineKeyboardButton("Лица и шеи", callback_data='Lica_i_shei')

    markup.add(item1, item2, item3, item4, item42)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Морщины"._\n\n'
                                           '*Морщины где?*', reply_markup=markup, parse_mode="Markdown")


def lob(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item13 = types.InlineKeyboardButton("Ботокс", callback_data='Botox')

    markup.add(item13)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Лоб"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def botox(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item30 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Botox_info')

    markup.add(item30)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Ботокс"._\n\n'
                                           '*Все морщины на лбу:* от 4200₽ до 7800₽\n'
                                           '*Межбровные морщины:* от 2400₽ до 3400₽',
                     reply_markup=markup, parse_mode="Markdown")


def botox_info(call):
    bot.send_message(call.message.chat.id, '*Ботулотоксин* блокирует нервные сигналы, '
                                           'которые в норме заставляют наши мышцы сокращаться. '
                                           'Мышца расслабляется и замирает, а сами морщины за '
                                           'счет этого сглаживаются. Эффект проявляется через несколько '
                                           'дней после инъекции, достигает пика на второй-третьей неделе '
                                           'и постепенно снижается через четыре-пять месяцев.',
                     parse_mode="Markdown")


def biorevit_info(call):
    bot.send_message(call.message.chat.id, '*Биоревитализация* это введение гиалуроновой кислоты '
                                           'под кожу, там она способна увлажнять, восстанавливать '
                                           'структуры межклеточного матрикса и стимулировать синтез '
                                           'коллагена и эластина. Инъекции гиалуроновой кислоты делают '
                                           'кожу заметно более плотной и упругой, сглаживают морщины и '
                                           'предотвращают появление сухости.',
                     parse_mode="Markdown")


def filler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item32 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Filler_info')

    markup.add(item32)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Филлер"._\n\n'
                                           '*Neauvia:* 10000₽', reply_markup=markup, parse_mode="Markdown")


def filler_info(call):
    bot.send_message(call.message.chat.id, '*Филлер* (от англ. to fill – наполнять) – гелевидный препарат '
                                           'на основе гиалуроновой кислоты для безоперационного '
                                           'омоложения, помогающий избавиться от глубоких морщин и '
                                           'последствий птоза (опущения тканей из-за гравитации). '
                                           'Филлер восполняет объем ''тканей и «поднимает» их.',
                     parse_mode="Markdown")


def vokrug_glaz(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item16 = types.InlineKeyboardButton("Ботокс", callback_data='Botox_other')
    item17 = types.InlineKeyboardButton("Биоревитализация", callback_data='Biorevit_other')

    markup.add(item16, item17)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Вокруг глаз"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def botox_other(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item30 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Botox_info')

    markup.add(item30)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Ботокс"._\n\n'
                                           '*Все морщины вокруг глаз:* от 2400₽ до 5600₽',
                     reply_markup=markup, parse_mode="Markdown")


def biorevit_other(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item31 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Biorevit_info')

    markup.add(item31)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Биоревитализация"._\n\n'
                                           '*Mesoeye C71:* 7000₽', reply_markup=markup, parse_mode="Markdown")


def nosogubnie(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item15 = types.InlineKeyboardButton("Филлер", callback_data='Filler')

    markup.add(item15)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Носогубные"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def vokrug_gub(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item15 = types.InlineKeyboardButton("Филлер", callback_data='Filler')

    markup.add(item15)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Вокруг губ"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def lica_i_shei(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item43 = types.InlineKeyboardButton("Биоревитализация", callback_data='Biorevit')

    markup.add(item43)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Лица и шеи"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def biorevit(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item31 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Biorevit_info')

    markup.add(item31)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Биоревитализация"._\n\n'
                                           '*Hyaron:* 4000₽\n'
                                           '*Femegyl Биолифт:* 6000₽', reply_markup=markup, parse_mode="Markdown")


# АКНЕ
def akne(call):
    # Картинка
    photo = open('static/akne.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item5 = types.InlineKeyboardButton("Пилинг", callback_data='Piling')
    item6 = types.InlineKeyboardButton("Чистка лица", callback_data='Chistka_lica')
    item7 = types.InlineKeyboardButton("Мезотерапия", callback_data='Mezoterapia')

    markup.add(item5, item6, item7)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Акне"._\n\n'
                                           '*Рекомендуемые процедуры* ↓', reply_markup=markup, parse_mode="Markdown")


def piling(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item8 = types.InlineKeyboardButton("Поверхностный", callback_data='Poverhnostniy')
    item9 = types.InlineKeyboardButton("Срединный", callback_data='Sredinniy')

    markup.add(item8, item9)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Пилинг"._\n\n'
                                           '*Виды пилинга* ↓', reply_markup=markup, parse_mode="Markdown")


def poverhnostniy(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item35 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Poverhnostniy_info')

    markup.add(item35)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Поверхностный"._\n\n'
                                           '*Миндальный:* 2500₽\n'
                                           '*Салициловый:* 2500₽\n'
                                           '*Гликолевый:* 2500₽\n'
                                           '*Пировиноградный:* 2500₽', reply_markup=markup, parse_mode="Markdown")


def poverhnostniy_info(call):
    bot.send_message(call.message.chat.id, '*Миндальный пилинг:* нормализует салоотделение, оказывает '
                                           'поросуживающее действие, устраняет комедоны,'
                                           'выравнивает цвет лица.\n\n'
                                           '*Салициловый пилинг:* растворяет сальные пробки, уменьшает '
                                           'салоотделение и нормализует состава себума, '
                                           'обладает антимикробным действием и способствует '
                                           'осветлению пигментных пятен постакне.\n\n'
                                           '*Гликолевый пилинг:* омоложение кожи за счет стимуляции '
                                           'активного синтеза фибропластов и коллагена, сглаживание '
                                           'кожного рельефа, устранение мелких морщин, '
                                           'противовоспалительное действие, уменьшение пигментации.\n\n'
                                           '*Пировиноградный:* осветляет пигментацию контролирует работу '
                                           'сальных желез, борется с комедонами стимулирует синтез '
                                           'коллагена и эластина, обладает антимикробным действием.',
                     parse_mode="Markdown")


def sredinniy(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item36 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Sredinniy_info')

    markup.add(item36)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Срединный"._\n\n'
                                           '*Prx-t33:* 3800₽\n'
                                           '*Armorique:* 3000₽\n'
                                           '*BioRePill:* 3000₽', reply_markup=markup, parse_mode="Markdown")


def sredinniy_info(call):
    bot.send_message(call.message.chat.id, '*Prx-t33:* решает сразу целый комплекс задач: 33% '
                                           'трихлоруксусная кислота оказывает противовоспалительное '
                                           'действие, борется с бактериями, стимулирует работу '
                                           'фибробластов, которые являются строительным материалом для '
                                           'выработки коллагена и эластина, а также очищает поры.5% '
                                           'койевая кислота осветляет пигментацию и неровный тон кожи.\n\n'
                                           '*Armorique:* восстановление рельефа и структуры кожного '
                                           'покрова, выравнивание тона и цвета кожи, сглаживание рубцов '
                                           'постакне, исчезновение гиперкератоза, осветление пигментных '
                                           'пятен, восстановление тонуса кожи.\n\n'
                                           '*BioRePill:* уникальность препарата в том, что он наносится и '
                                           'действует как пилинг, но при этом дает эффект '
                                           'биоревитализации, но при этом без инъекций, следов от '
                                           'процедуры и реабилитационного периода. Всего за одну '
                                           'процедуру вы получите мгновенный лифтинг, осветление '
                                           'пигментных пятен и уплотнение кожи.', parse_mode="Markdown")


def chistka_lica(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item40 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Chistka_lica_info')

    markup.add(item40)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Чистка лица"._\n\n'
                                           '*Чистка с химическим пилингом:* 3500₽\n'
                                           '*Ультразвуковая чистка:* 2800₽', reply_markup=markup, parse_mode="Markdown")


def chistka_lica_info(call):
    bot.send_message(call.message.chat.id, '*Механическая чистка:* проводится путем механического удаления '
                                           'кожного сала специальными инструментами и руками.\n\n'
                                           '*Химическая чистка:* подразумевает удаление поверхностных '
                                           'слоев эпидермиса специфическими растворами кислот.\n\n'
                                           '*Ультразвуковая чистка:* очищение кожи выполняется путем '
                                           'воздействия ультразвуковых волн.', parse_mode="Markdown")


def mezoterapia(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item41 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Mezoterapia_info')

    markup.add(item41)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Мезотерапия"._\n\n'
                                           '*Локальное введение антибактериального препарата:* 300₽\n'
                                           '*Мезотерапия Анти-акне:* 1500₽', reply_markup=markup, parse_mode="Markdown")


def mezoterapia_info(call):
    bot.send_message(call.message.chat.id, '*Мезотерапия Анти-акне:* угнетает рост бактерий, являющихся '
                                           'главной причиной акне, снижает активность 5а-редуктазы и '
                                           'уменьшает покраснение кожи, улучшает обновление тканей, '
                                           'успокаивает раздраженную кожу и уменьшает покраснения.',
                     parse_mode="Markdown")


# ВЫПАДЕНИЕ ВОЛОС
def vipadenie(call):
    # Картинка
    photo = open('static/vipadenie.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item20 = types.InlineKeyboardButton("Мезотерапия", callback_data='Mezoterapia_dermaheal')

    markup.add(item20)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Выпадение волос"._\n\n'
                                           '*Вам подойдёт* ↓', reply_markup=markup, parse_mode="Markdown")


def mezoterapia_dermaheal(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item34 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Mezoterapia_dermaheal_info')

    markup.add(item34)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Мезотерапия"._\n\n'
                                           '*Dermaheal HL:* 1500₽\n'
                                           '*Hair X Peptide:* 3000₽', reply_markup=markup, parse_mode="Markdown")


def mezoterapia_dermaheal_info(call):
    bot.send_message(call.message.chat.id, '*Мезотерапия* для лечения волос и кожи головы – это инъекции '
                                           'специальных коктейлей, которые доставляются прямо к волосяным '
                                           'фолликулам с целью лечения выпадения волос, улучшения их '
                                           'роста, восстановления структурных повреждений волос и '
                                           'оздоровления кожи головы.', parse_mode="Markdown")


# ПИГМЕНТАЦИЯ
def pigmentacia(call):
    # Картинка
    photo = open('static/pigmentacia.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item10 = types.InlineKeyboardButton("Пилинг", callback_data='Piling_pigment')
    item11 = types.InlineKeyboardButton("Мезотерапия", callback_data='Mezoterapia_pigment')

    markup.add(item10, item11)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Пигментация"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def piling_pigment(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item12 = types.InlineKeyboardButton("Поверхностный", callback_data='Poverhnostniy_pigment')
    item9 = types.InlineKeyboardButton("Срединный", callback_data='Sredinniy')

    markup.add(item12, item9)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Пилинг"._\n\n'
                                           '*Виды пилинга* ↓', reply_markup=markup, parse_mode="Markdown")


def poverhnostniy_pigment(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item37 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Poverhnostniy_pigment_info')

    markup.add(item37)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Поверхностный"._\n\n'
                                           '*Гликолевый пилинг:* 2500₽', reply_markup=markup, parse_mode="Markdown")


def poverhnostniy_pigment_info(call):
    bot.send_message(call.message.chat.id, '*Гликолевый пилинг:* омоложение кожи за счет стимуляции '
                                           'активного синтеза фибропластов и коллагена, сглаживание '
                                           'кожного рельефа, устранение мелких морщин, '
                                           'противовоспалительное действие, уменьшение пигментации.',
                     parse_mode="Markdown")


def mezoterapia_pigment(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item38 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Mezoterapia_pigment_info')

    markup.add(item38)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Мезотерапия"._\n\n'
                                           '*F-radiance:* 1500₽', reply_markup=markup, parse_mode="Markdown")


def mezoterapia_pigment_info(call):
    bot.send_message(call.message.chat.id, '*F-radiance:* '
                                           'результатом применения является сокращение альфа-активности '
                                           'тирозиназы (фермент ответственный за пигментацию). Стимулирует '
                                           'обновление кожи, улучшение цвета кожи, нейтрализует свободные '
                                           'радикалы, уменьшает появление темных точек.', parse_mode="Markdown")


# ПОСТАКНЕ
def postakne(call):
    # Картинка
    photo = open('static/postakne.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item8 = types.InlineKeyboardButton("Пилинг", callback_data='Piling_pigment')
    item19 = types.InlineKeyboardButton("Мезотерапия", callback_data='Mezoterapia_pigment')
    item21 = types.InlineKeyboardButton("Карбокситерапия", callback_data='Carboxi')

    markup.add(item8, item19, item21)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Постакне"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def carboxi(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item39 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Carboxi_info')

    markup.add(item39)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Карбокситерапия"._\n\n'
                                           '*Неинвазивная:* 1800₽', reply_markup=markup, parse_mode="Markdown")


def carboxi_info(call):
    bot.send_message(call.message.chat.id, '*Карбокситерапия неинвазивная:* выравнивание тона лица, '
                                           'а именно: фотостарение, акне и постакне, рубцовая ткань, '
                                           'пигментные пятна, лифтинг кожи, отбеливание кожи.',
                     parse_mode="Markdown")


# ВТОРОЙ ПОДБОРОДОК
def zhirovie_otlozheniya(call):
    # Картинка
    photo = open('static/zhirovie_otlozheniya.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item40 = types.InlineKeyboardButton("Липолитики", callback_data='Lipolitiki_zhir')

    markup.add(item40)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Жировые отложения"._\n\n'
                                           '*Выберите процедуру* ↓', reply_markup=markup, parse_mode="Markdown")


def lipolitiki_zhir(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item41 = types.InlineKeyboardButton("Подробнее o процедуре", callback_data='Lipolitiki_zhir_info')

    markup.add(item41)
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Липолитики"._\n\n'
                                           '*Непрямые липолитики:* от 2500₽', reply_markup=markup,
                     parse_mode="Markdown")


def lipolitiki_zhir_info(call):
    bot.send_message(call.message.chat.id, '*Непрямой липолитик* – это препарат, который превращает жир в воду, '
                                           'а вода уже выводится из организма по системе микрососудов. '
                                           'Назначают липолитики как финальную часть комплексной терапии, '
                                           'чтобы убрать зоны-ловушки: жировые складки над коленями, '
                                           'небольшое количество жира на животе или под подбородком, '
                                           'галифе на бедрах. Важно при этом соблюдать и другие рекомендации: '
                                           'например, режим питания и тренировок.', parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'К началу ↑':
            welcome_new(message)
        elif message.text == '☎ Записаться на процедуру':
            my_info(message)
        else:
            bot.send_message(message.chat.id, 'Выберите один вариант из предложенных выше, пожалуйста.')


# RUN
bot.polling(none_stop=True)
