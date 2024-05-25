# main.py

import discord
from discord.ext import commands
from settings import Settings
from bot import Bot

# Initialize bot settings
settings = Settings()
bot = Bot(settings)

# Create a new Discord bot instance
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=settings.prefix, intents=intents)

# Load and run the bot
@bot.event
async def on_ready():
    print(f'Bot is ready and logged in as {bot.user}')

# Run the bot with the specified token
bot.run(settings.token)