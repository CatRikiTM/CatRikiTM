from pyrogram import Client, filters
from pyrogram.errors import FloodWait, SlowmodeWait, ChannelPrivate
from pyrogram.raw import functions
import sqlite3
import sys
from datetime import datetime
import logging
import pyrogram
import random
import asyncio

app = Client("my_account")

def reply(func):
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except SlowmodeWait as sw:
            if sw.x > 30:
                logging.info(f'Script wont sleep {sw.x}s - >30s ({sw})')
                return
            logging.warning(f'Sleeping {sw.x}s due to {sw}')
            await sleep(sw.x)
            await func(*args, **kwargs)
        await asyncio.sleep(0.25)

    return wrapper

class TextPost:
    def __init__(self, text):
        self.text = text

    @reply
    async def reply_to(self, message):
        await message.reply_text(self.text)

class RandomPost:

    def __init__(self, *args):
        self.posts = args

    async def reply_to(self, message):
        await random.choice(self.posts).reply_to(message)
        
spam_from_channel = False
# Chat (Sender) - stores chat from which bot will spam (profile or channels)
send_chat = None
# Using to avoid media group bug
last_media_group = 123
# Spam Posts - stores posts to spam, supported types: TextPost, PicturePost, StickerPost, RandomPost
spam_posts = [RandomPost(TextPost("Извините, но игра Brawl Stars больше не поддерживается в вашем регионе."), TextPost("Ваш IP состоит в списке запрещённых стран."))]        
        
sys.tracebacklimit = 0
pyrogram_logging = logging.WARNING
userbot_logging = logging.INFO
logging.basicConfig(level=pyrogram_logging)
logger = logging.getLogger("userbot")
logger.setLevel(userbot_logging)


# TODO: Логи ошибок
@app.on_message(filters.channel)
async def answer(_, message):
    global last_media_group
    message_log = message.text.replace("\n", "")[:40] + '..' if message.text is not None else str()
    if message.edit_date is None or (
            datetime.utcfromtimestamp(message.edit_date) - datetime.utcfromtimestamp(message.date)).total_seconds() > 5:
        logger.debug(f"|{message.chat.title}|Skipping message. (edit date: {message.edit_date})")
        return
    if last_media_group == message.media_group_id and message.media_group_id is not None:
        logger.debug(f"|{message.chat.title}|Skipping message. (media group: last - {last_media_group}, message - {message.media_group_id}).")
        return
    logger.info(f"|{message.chat.title}|:Caught message. (Text: {message_log})")
    last_media_group = message.media_group_id
    linked = await get_linked(message)
    message_to_answer = await get_forwarded_in_linked(message.message_id, linked)
    if message_to_answer is None:
        logger.error(f"|{message.chat.title}|:Banned or couldn't get comments.")
        return
    if spam_from_channel:
        await init_sender(linked.id)
        await app.set_send_as_chat(linked.id, send_chat.id)

    for post in spam_posts:
        await post.reply_to(message_to_answer)

    logger.info(f"|{message.chat.title}|:Answered.")


async def get_forwarded_in_linked(message_id, linked): # TODO: Check for forwarded_from_id
    try:
        async for message in app.search_messages(linked.id, limit=1, filter="pinned"):
            return message
    except ChannelPrivate:
        return None

async def init_sender(_chat):
    # TODO: Enter = default, Error logs
    global send_chat
    if send_chat:
        return

    chats = await app.get_send_as_chats(_chat)
    print("Available chats (0 - default):")
    for index, chat in enumerate(chats):
        chat_name = chat.title if chat.first_name is None else chat.first_name
        print(f"{index}: {chat_name}")
    try:
        _id = int(input("Write the number of the chat to spam then press Enter: "))
        send_chat = chats[_id]
    except ValueError:
        send_chat = chats[0]


async def get_linked(msg):
    channel = await app.get_chat("@pashampanov")
    return channel .linked_chat

try:
    text = 'Started!' if not spam_from_channel \
        else 'Started! Wait for a new message to set up the bot.'
    logger.info(text)
    app.run()
except ValueError:
    logger.error("The config.ini is configured incorrectly!")
                            
app.run()
