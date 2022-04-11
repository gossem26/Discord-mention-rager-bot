import discord, random, asyncio, os
from discord.ext import commands


client = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
response_mtime = 0
responses = []

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
	global response_mtime, responses
	if(message.mention_everyone == True or str(client.user.id) in message.content):
		if(os.stat("responses.txt").st_mtime != response_mtime):
			print("responses updated")
			response_mtime = os.stat("responses.txt").st_mtime
			with open("responses.txt", 'r') as r:
				responses = r.readlines()
		async with message.channel.typing():
			await asyncio.sleep(4)
			await message.channel.send(responses[random.randrange(len(responses))])

with open("token.txt", 'r') as t:
	client.run(t.read())

