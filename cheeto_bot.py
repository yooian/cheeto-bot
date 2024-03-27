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

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

# Bot commands
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.command()
async def copy(ctx, arg):
    await ctx.send(arg)

client.run(TOKEN)

#... continue work