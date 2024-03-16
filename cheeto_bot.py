import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

# Get token for bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#... continue work