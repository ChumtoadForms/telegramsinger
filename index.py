from time import sleep
from config import conf
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

# СЛЕДУЮЩИЕ ДВЕ СТРОЧКИ НЕ МЕНЯТЬ, В ПРОТИВНОМ СЛУЧАЕ ВСЁ СЛОМАЕТСЯ
api_id = 18539672
api_hash = 'c9cee400e328a55aacec41f7d19d8743'

lines = []

with open('song', 'r', encoding='utf-8') as f:
	for line in f:
		line = line.strip()
		if len(line) == 0:
			continue
		if conf["use_caps"]:
			line = line.to_upper()
		lines.append(line)

client = Client('userbot pyrogram', api_id, api_hash)

client.start()
client.stop()
print('Бот запущен. Пой песню)')

@client.on_message(filters.regex('Хочешь песню?') & filters.me)
def typesong(client, message):
	sleep(3)
	for i in range(0, len(lines)):
		client.send_message(message.chat.id, lines[i])
		sleep(conf["interval"])

client.run()
