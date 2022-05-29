from telethon import TelegramClient

from config import *
import psycopg2
import datetime
import telethon
import asyncio

from bd import BotDB
BotDB = BotDB(db_uri)

async def main():
    client = TelegramClient('main_session', api_id, api_hash)
    client = await client.start()

    my_channel = await client.get_entity(channel1_id)

    members_telethon_list = await client.get_participants(my_channel)


    for member in members_telethon_list:
        if not member.bot:
            BotDB.cursor.execute(f"SELECT users_id FROM userschannel WHERE users_id = {member.id}")
            result = BotDB.cursor.fetchone()

            if not result:
                BotDB.add_data(member.id, member.username, member.first_name, member.last_name, member.phone,
                                datetime.datetime.today().day)

async def task():
    await main()

asyncio.get_event_loop().run_until_complete(task())