from pyrogram.errors import FloodWait, SlowmodeWait
import time as t
from datetime import datetime, timedelta
import random
import pytz
from PIL import Image, ImageDraw, ImageFont
import tgcrypto
from gtts import gTTS
from pyrogram.raw import functions
import asyncio
import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from io import BytesIO

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
		
@app.on_message(filters.command(["calc"], prefixes="."))	
async def calc(_, message: Message):
    if len(message.command) <= 1:
        return
    args = " ".join(message.command[1:])
    try:
        result = str(eval(args))

        if len(result) > 4096:
            i = 0
            for x in range(0, len(result), 4096):
                if i == 0:
                    await message.edit(
                        f"<i>{args}</i><b>=</b><code>{result[x:x + 4000]}</code>",
                        parse_mode="HTML",
                    )
                else:
                    await message.reply(
                        f"<code>{result[x:x + 4096]}</code>", parse_mode="HTML"
                    )
                i += 1
                await asyncio.sleep(0.18)
        else:
            await message.edit(
                f"<i>{args}</i><b>=</b><code>{result}</code>", parse_mode="HTML"
            )
    except Exception as e:
        await message.edit(f"<i>{args}=</i><b>=</b><code>{e}</code>", parse_mode="HTML")

@app.on_message(filters.command(["dem"], prefixes="."))    
async def demotivator(client: Client, message: Message):
    await message.edit("<code>Выполняется🌀...</code>")
    font = requests.get(
        "https://github.com/Dragon-Userbot/files/blob/main/Times%20New%20Roman.ttf?raw=true"
    )
    f = font.content
    template_dem = requests.get(
        "https://raw.githubusercontent.com/Dragon-Userbot/files/main/demotivator.png"
    )
    if message.reply_to_message:
        words = ["хахаха лох", "обед!", "хохл момент", "чо"]
        if message.reply_to_message.photo:
            donwloads = await client.download_media(
                message.reply_to_message.photo.file_id
            )
            photo = Image.open(f"{donwloads}")
            resize_photo = photo.resize((469, 312))
            text = (
                message.text.split(" ", maxsplit=1)[1]
                if len(message.text.split()) > 1
                else random.choice(words)
            )
            im = Image.open(BytesIO(template_dem.content))
            im.paste(resize_photo, (65, 48))
            text_font = ImageFont.truetype(BytesIO(f), 22)
            text_draw = ImageDraw.Draw(im)
            text_draw.multiline_text(
                (299, 412), text, font=text_font, fill=(255, 255, 255), anchor="ms"
            )
            im.save(f"downloads/{message.message_id}.png")
            await message.reply_to_message.reply_photo(
                f"downloads/{message.message_id}.png"
            )
            await message.delete()
        elif message.reply_to_message.sticker:
            if not message.reply_to_message.sticker.is_animated:
                donwloads = await client.download_media(
                    message.reply_to_message.sticker.file_id
                )
                photo = Image.open(f"{donwloads}")
                resize_photo = photo.resize((469, 312))
                text = (
                    message.text.split(" ", maxsplit=1)[1]
                    if len(message.text.split()) > 1
                    else random.choice(words)
                )
                im = Image.open(BytesIO(template_dem.content))
                im.paste(resize_photo, (65, 48))
                text_font = ImageFont.truetype(BytesIO(f), 22)
                text_draw = ImageDraw.Draw(im)
                text_draw.multiline_text(
                    (299, 412), text, font=text_font, fill=(255, 255, 255), anchor="ms"
                )
                im.save(f"downloads/{message.message_id}.png")
                await message.reply_to_message.reply_photo(
                    f"downloads/{message.message_id}.png"
                )
                await message.delete()
            else:
                await message.edit("<b>Прости, анимационные стикеры неподдерживаются</b>")
        else:
            await message.edit("<b>Реплай на фото/стикер.</b>")
    else:
        await message.edit("<b>Реплай на фото/стикер.</b>")

 async def make(client, message, o):
    reply = message.reply_to_message
    if reply.photo or reply.sticker:
        if reply.photo:
            downloads = await client.download_media(reply.photo.file_id)
        else:
            downloads = await client.download_media(reply.sticker.file_id)
        path = f"{downloads}"
        img = Image.open(path)
        await message.delete()
        w, h = img.size
        if o in [1, 2]:
            if o == 2:
                img = ImageOps.mirror(img)
            part = img.crop([0, 0, w // 2, h])
            img = ImageOps.mirror(img)
        else:
            if o == 4:
                img = ImageOps.flip(img)
            part = img.crop([0, 0, w, h // 2])
            img = ImageOps.flip(img)
        img.paste(part, (0, 0))
        img.save(path)
        if reply.photo:
            return await reply.reply_photo(photo=path)
        elif reply.sticker:
            return await reply.reply_sticker(sticker=path)
        os.remove(path)

    return await message.edit("<b>Реплай на фото.</b>")

@app.on_message(filters.command(["отразить1", "отразить2", "отразить3", "отразить4"], prefixes="."))
async def mirror_flip(client: Client, message: Message):
    await message.edit("<b>Processing...</b>")
    param = {"отразить1": 1, "отразить2": 2, "отразить3": 3, "отразить4": 4}[message.command[0]]
    param = {"отразить1": 1, "отразить2": 2, "отразить3": 3, "отразить4": 4}[message.command[0]]													
													
app.run()
