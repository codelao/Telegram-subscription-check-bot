from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btnProfile = KeyboardButton('Profile')
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(btnProfile)


btnUrl = InlineKeyboardButton(text='Subscribe', url='https://t.me/codelao1')
btnsubdone = InlineKeyboardButton(text='Check subscription', callback_data='subdone')
checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrl)
checkSubMenu.insert(btnsubdone)
