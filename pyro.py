

from pyrogram import Client, filters
from gtts import gTTS
import datetime
import requests
import random
import asyncio
import config
import json
import time
import os

app = Client("my_account")

@app.on_message(filters.command(["web"], prefixes="."))
async def vzlom(client, message):
	   try:
	   	old_link = message.text.split()[1]
	   except:
	   	await message.reply("<b>Еблан! Надо так! .web (сайт)</b>")
	   	return
	   new_link = 'https://webshot.deam.io/{}/?width=1920&height=1080?type=png'.format(old_link)
	   try:
	   	await app.send_photo(message.chat.id, new_link, caption=f'<b>✅ Вот твой скрин от сайта: {old_link}</b>')
	   except:
	   	await message.reply("❌ Не удалось сделать скриншот сайта!")
	   
	       		
app.run()


