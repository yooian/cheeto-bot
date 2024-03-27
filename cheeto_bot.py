import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

# Get token for bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Necessary for bot to receive messages
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# Bot commands
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(TOKEN)

#... continue work