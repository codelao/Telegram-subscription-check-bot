from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnProfile = KeyboardButton('Профиль')
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(btnProfile)

#subscribe buttons
btnUrl = InlineKeyboardButton(text='Подписаться', url='https://t.me/...')
btnsubdone = InlineKeyboardButton(text='Проверить подписку', callback_data='subdone')
checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrl)
checkSubMenu.insert(btnsubdone)