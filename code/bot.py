import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

TOKEN = ''
CHANNEL_ID = '@...'
NOT_SUB = 'Subscribe to this channel first'
ANOTHER_NOT_SUB = 'Subscription not found'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#return True if user is subscribed
def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Hi there👋', reply_markup=nav.profileKeyboard)
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        #if user will try to write 'Profile' without subscription
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            if message.text == 'Profile':
                await bot.send_message(message.from_user.id, "📃Your profile: " + message.from_user.first_name)
            else:
                await bot.send_message(message.from_user.id, 'Unknown command')
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)


@dp.callback_query_handler(text='subdone')
async def subdone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Hi there👋', reply_markup=nav.profileKeyboard)
    else:
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
