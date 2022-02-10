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
		client.send_message(message.chat.id, 1s)
		client.send_message(message.chat.id, 2s)
		client.send_message(message.chat.id, 3s)
		client.send_message(message.chat.id, 4s)
		client.send_message(message.chat.id, 5s)
		client.send_message(message.chat.id, 6s)
		client.send_message(message.chat.id, 7s)
		client.send_message(message.chat.id, 8s)

client.run()
