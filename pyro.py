from pyrogram import Client, filters
from pyrogram.errors import FloodWait, SlowmodeWait
import time as t
from datetime import datetime, timedelta
import random
import pytz
from PIL import Image, ImageFilter
import tgcrypto
from gtts import gTTS
from pyrogram.raw import functions
import asyncio
import os
import requests

app = Client("my_account") 

@app.on_message(filters.command(["vzlom"], prefixes="."))
async def vzlom(client, message):
		if not message.reply_to_message:
			await app.send_message(message.chat.id, 'Это не реплай!', reply_to_message_id=message.message_id)
			return
		if message.reply_to_message.from_user.id == 1451300395:
			await app.send_message(message.chat.id, "Жопу создателя нельзя взломать!", reply_to_message_id=message.message_id)
			return
		vzlom = await app.send_message(message.chat.id, 'Взлом жопы...🌀', reply_to_message_id=message.message_id)
		await asyncio.sleep(1)
		await app.edit_message_text(message.chat.id, vzlom.message_id, f'**Жопа [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) успешно взломана!**')
	   
app.run() 

@app.on_message(filters.command(["spam"], prefixes=".") & filters.me)
async def spam(client, message):
	text = message.text.split()
	text.remove(".spam")
	count = text[len(text)-1]
	text.remove(text[len(text)-1])
	text_str = ' '.join(text)
	try:
		for spam in range(0, int(count)):
			await app.send_message(message.chat.id, text_str)
	except FloodWait:
		await asyncio.sleep(e.x)

	   
			



