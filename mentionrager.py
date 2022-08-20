#BSD 3-Clause License
#
#Copyright (c) 2022, gossem26
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import discord, random, asyncio, os, argparse
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)
response_mtime = 0
responses = []
parser = argparse.ArgumentParser(description="A Discord bot that sends an angry message every time someone mentions @ everyone")
parser.add_argument("-r", default="responses.txt", help="path for a pesponses file. default=responses.txt")
args = parser.parse_args()
response_file=args.r
try:
	with open(response_file, 'r') as r:
		responses = r.readlines()
except:
	print("failed to open $s, defaulting to responses.txt")
	response_file="responses.txt"
	with open(response_file, 'r') as r:
		responses = r.readlines()
@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
	global response_mtime, responses
	if(message.mention_everyone == True or str(client.user.id) in message.content):
		if(os.stat(response_file).st_mtime != response_mtime):
			print("responses updated")
			response_mtime = os.stat(response_file).st_mtime
			with open(response_file, 'r') as r:
				responses = r.readlines()
		async with message.channel.typing():
			await asyncio.sleep(4)
			await message.channel.send(responses[random.randrange(len(responses))])

with open("token.txt", 'r') as t:
	client.run(t.read())

