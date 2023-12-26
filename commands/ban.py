import discord 
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member : discord.Member, reason=None):
        await member.ban(reason=reason)

async def setup(bot : commands.Bot=None):
    await bot.add_cog(ban(bot))

    