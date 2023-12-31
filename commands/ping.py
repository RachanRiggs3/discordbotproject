import discord 
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong!, The Latency Of the bot is {round(self.bot.latency * 1000)}")

async def setup(bot: commands.Bot):
    await bot.add_cog(ping(bot))