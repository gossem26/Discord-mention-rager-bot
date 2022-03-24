import discord
from discord.ext import commands
import random

responses = ["What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.",
"why the fuck did you mention everyone, you piece of shit? you have nothing better to do than be annoying? you didn't even send anything that important! I hope you wake up with back pains every day. eat shit and die asshole!",
"I hate croissants. I hate cinnamon rolls. I hate pizza. I hate mozzarella and tomato sandwiches on fresh focaccia I hate baguette with fancy soft cheese. I hate fettuccine alfredo with crispy shrimp on top and I hate eggs benedict over whole grain English muffins. Biscuits with butter make me gag. Beef noodle soup? Ew! And I hate chocolate chip cookies and fluffy blueberry muffins and yes, I even hate brownies. Fucking despise them. Revolting. Hope I never have to eat another brownie sundae with hot fudge and homemade maple whipped cream ever again, SO GROSS. wheat makes things so flaky or crumbly or fluffy and it's just vile, why can't everyone see this? I FUCKING HATE WHEAT!!!!!!!!!!!!!!",
"You fat bald bastard! You piece of subhuman trash! Two-thousand years of constant human evolution to create a hairless FUCKING COCONUT MY GOD WHAT OS WRONG WITH YOU???"]
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    if(message.mention_everyone == True):
        await message.channel.send(responses[random.randrange(len(responses))])

client.run(open("token.txt", 'r').read())
