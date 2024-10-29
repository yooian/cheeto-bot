import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

import random
import psycopg2 # PostgreSQL

# Get token for bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Set up database connection
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    host=DB_HOST,
    password=DB_PASSWORD
)

# Description
description = "A bot to send and get images of cheeto!"

# Necessary for bot to receive messages
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

# Bot commands
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# async def copy(ctx, arg):
#     await ctx.send(arg)

# @bot.command()
# async def meow(ctx, arg=1):
#     meow = ""
#     for _ in range(0, arg):
#         meow += "MEOW "
#     await ctx.send(meow)
    
# @meow.error
# async def meow_error(ctx, error):
#     if isinstance(error, commands.BadArgument):
#         await ctx.send('I can only meow if you give me a number mf')

@bot.command()
>>>>>>> main:src/cheeto_bot.py
async def cheeto(ctx):
  with connection.cursor() as cursor:
    cursor.execute("SELECT url FROM cheetos ORDER BY RANDOM() LIMIT 1;")
    result = cursor.fetchone()
    if result:
        await ctx.send(result[0])
    else:
        await ctx.send("No Cheetos found :(")
  
bot.run(TOKEN)