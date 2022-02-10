from time import sleep
from config import *
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

client = Client('userbot pyrogram', api_id, api_hash)

client.start()
client.stop()
print('Бот запущен. Пой песню)')

@client.on_message(filters.regex('Хочешь песню?') & filters.me)
def typesong(client, message):
	i = 0
	while i < 7:
		i += 1
		client.send_message(message.chat.id, songtext.readline())

client.run()