import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

# Get token for bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Description
description = "A bot to send and get images of cheeto!"

# Necessary for bot to receive messages
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

# Bot commands
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def copy(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def meow(ctx, arg=1):
    meow = ""
    for _ in range(0, arg):
        meow += "MEOW "
    await ctx.send(meow)
    
@meow.error
async def meow_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I can only meow if you give me a number mf')

bot.run(TOKEN)