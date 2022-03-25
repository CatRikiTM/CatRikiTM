from pyrogram.errors.exceptions import ChannelPrivate
from datetime import datetime, timedelta
import sys
import logging
from pyrogram import Client, filters
import asyncio
from pyrogram.errors import FloodWait, SlowmodeWait
import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Client("my_account")

GROM = "@bschatt"

with app:
    app.send_message(GROM, "Ben.")

@app.on_message(filters.chat(GROM))
def echo(client, message):
    message.reply(message.text)
