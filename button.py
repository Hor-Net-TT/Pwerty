from telebot import types


def welcome():
    MainPanel = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    ).add(
        types.KeyboardButton(text='Температуры водоемов')
    ).add(
        types.KeyboardButton(text='О нас'),
        types.KeyboardButton(text='Языки')
    )

    return MainPanel


def about():
    AboutPanel = types.InlineKeyboardMarkup(

    ).add(
        types.InlineKeyboardButton(text='Канал', url='t.me/kuslovick')
    ).add(
        types.InlineKeyboardButton(text='Помощь', url='t.me/HorKBit')
    )

    return AboutPanel


def languages():
    LanguagesPanel = types.InlineKeyboardMarkup(

    ).add(
        types.InlineKeyboardButton(text='Русский🇷🇺', callback_data='russian')
    ).add(
        types.InlineKeyboardButton(text='English🇬🇧', callback_data='english')
    ).add(
        types.InlineKeyboardButton(text='Український🇺🇦', callback_data='ukrainian')
    )

    return LanguagesPanel