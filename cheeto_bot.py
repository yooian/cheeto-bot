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
    for _ in range(0, arg):
        await ctx.send("MEOW")

@bot.command()
async def cheeto(ctx):
  await ctx.send(ctx.message.attachments[0].url)
  await ctx.send("PICTURE RECEIVED")
  
bot.run(TOKEN)