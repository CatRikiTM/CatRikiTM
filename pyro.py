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
from pyrogram import Client, filters
from pyrogram.types import Message
from io import BytesIO
import shutil
from decimal import getcontext, Decimal
from typing import List, Optional, Tuple, Union
from glitch_this import ImageGlitcher


app = Client("my_account", api_id=11684516, api_hash="6d80a20f13e07684e51c1d914ef59503"
)



		
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
	
spam_text = 'ого'
used_filters = filters.channel
	
@app.on_message(used_filters)
async def klalsls(_, message):
	if message.edit_date is None or (
            datetime.utcfromtimestamp(message.edit_date) - datetime.utcfromtimestamp(message.date)).total_seconds() > 5:
		return
	linked = await get_linked(message)
	await asyncio.sleep(0.25)
	nsg = await app.get_history(linked, limit=1)
	await asyncio.sleep(0.25)
	await nsg[0].reply_text(spam_text)
	await asyncio.sleep(0.25)
	print("хуй: " + message.chat.title)

async def get_linked(nsg):
	channel = await app.get_chat(nsg.sender_chat.id)
	return channel.linked_chat.id

	
	

app.run()
