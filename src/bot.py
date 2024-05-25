# bot.py

import discord
from discord.ext import commands

from moderation import Moderation
from settings import Settings

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')
        self.moderation = Moderation()
        self.settings = Settings()

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        await self.moderation.mute_member(ctx, member)

    @commands.command()
    async def kick(self, ctx, member: discord.Member):
        await self.moderation.kick_member(ctx, member)

    @commands.command()
    async def ban(self, ctx, member: discord.Member):
        await self.moderation.ban_member(ctx, member)

    @commands.command()
    async def warn(self, ctx, member: discord.Member, reason: str):
        await self.moderation.warn_member(ctx, member, reason)

    @commands.command()
    async def set_auto_moderation(self, ctx, enabled: bool):
        await self.settings.set_auto_moderation(ctx, enabled)

    @commands.command()
    async def set_logging_channel(self, ctx, channel: discord.TextChannel):
        await self.settings.set_logging_channel(ctx, channel)

bot = Bot()
bot.run('your_bot_token')