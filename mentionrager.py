import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
	if(message.mention_everyone == True or str(client.user.id) in message.content):
		async with message.channel.typing():
			await asyncio.sleep(4)
			with open("responses.txt", 'r') as r:
				responses = r.readlines()
				await message.channel.send(responses[random.randrange(len(responses))])

with open("token.txt", 'r') as t:
	client.run(t.read())
