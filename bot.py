from aiogram import executor, types
from aiogram import types
from aiogram import Bot, Dispatcher
from config import *
from bd import BotDB
import datetime

bot = Bot(TOKEN)
dp = Dispatcher(bot)

BotDB = BotDB(db_uri)

@dp.message_handler(commands=['start'])
async def is_bot_working(message : types.Message):
    await bot.send_message(my_chat_id, 'Проверка бота! Бот запущен!')

@dp.channel_post_handler()
async def ban_member(message : types.Message):
    BotDB.cursor.execute("SELECT users_id from userschannel")
    result_id = BotDB.cursor.fetchall()
    counter = len(result_id)

    BotDB.cursor.execute("SELECT join_day from userschannel")
    result_day = BotDB.cursor.fetchall()

    BotDB.cursor.execute("SELECT usernames from userschannel")
    result_usernames = BotDB.cursor.fetchall()

    BotDB.cursor.execute("SELECT first_names from userschannel")
    result_fNames = BotDB.cursor.fetchall()

    BotDB.cursor.execute("SELECT last_names from userschannel")
    result_lNames = BotDB.cursor.fetchall()

    BotDB.cursor.execute("SELECT phones from userschannel")
    result_phones = BotDB.cursor.fetchall()

    if counter != 0:
        for i in range(0, counter):
            if datetime.datetime.today().day - result_day[i][0] == 7:
                await bot.ban_chat_member(message.chat.id, result_id[i][0])
                BotDB.delete_data(result_id[i][0], result_usernames[i][0], result_fNames[i][0], result_lNames[i][0],
                                  result_phones[i][0], result_day[i][0])

    if counter == 0:
        await bot.send_message(my_chat_id, 'Пользователи успешно удалены!')

executor.start_polling(dp, skip_updates=True)





