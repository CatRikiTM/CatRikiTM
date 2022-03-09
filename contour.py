@app.on_message(filters.command(["contour"], prefixes="."))
async def hui(Client, message):
        size = (128, 128)
        path = "shakal.png"
        if message.reply_to_message:
        	try:
        		await app.download_media(message.reply_to_message.photo, file_name=path, block=True)
        		original = Image.open('downloads/shakal.png')
        		original.thumbnail(size)
        		blurred_original = original.filter(ImageFilter.CONTOUR)
        		blurred_original.save('saved/shakal.png')
        		blurred_original.show()
        		await app.send_message(message.chat.id, "**🌀Выполняется...🌀**")
        		await asyncio.sleep(1)
        		await app.send_photo(message.chat.id, "saved/shakal.png", caption="**Вот твоё фото✅**", reply_to_message_id=message.message_id)
        	except AttributeError:
        		return await app.send_message(message.chat.id, "В реплае нет фото.")
        		os.remove("downloads/shakal.png")
        		os.remove("saved/shakal.png")
