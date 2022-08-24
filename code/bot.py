import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

TOKEN = '...'
CHANNEL_ID = '@...'
NOT_SUB = 'Сначала подпишитесь на этот канал'
ANOTHER_NOT_SUB = 'Подписка не найдена, попробуйте ещё раз'

logging.basicConfig(level=logging.INFO)

#Bot initialization
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

###Subscribe checking###
def check_sub(chat_member):
    #если пользователь - учаcтник канала, то его статус не равен left и возвращаем True, если status == left, то возвращаем False, так как пользователь не подписан на канал
    if chat_member['status'] != 'left':
        return True
    else:
        return False


#start message
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Добро пожаловать!👋', reply_markup=nav.profileKeyboard)
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)

#commands
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        #if user will try to write 'Профиль' by himself
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            if message.text == 'Профиль':
                await bot.send_message(message.from_user.id, "📃Ваш профиль: " + message.from_user.first_name)
            else:
                await bot.send_message(message.from_user.id, 'Я не знаю такой команды/слова😔')
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)



@dp.callback_query_handler(text='subdone')
async def subdone(message: types.Message):
    #delete message with sub buttons and open bot menu after subscribing
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Добро пожаловать!👋', reply_markup=nav.profileKeyboard)
    else:
        #send other text if sub is still not found
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)