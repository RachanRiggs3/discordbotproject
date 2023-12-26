import discord
from discord.ext import commands
import requests
import json

class catfact(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def catfact(self, ctx):
        catsfact_request = requests.get("https://catfact.ninja/fact")
        catfact_dict = json.loads(catsfact_request.text)
        catfact = catfact_dict["fact"]
        embed = discord.Embed(
            title="Cat facts by some free api lol",
            description=catfact,
            color=discord.Colour.blurple()
        )
        embed.set_footer(text=f"{ctx.author}")
        await ctx.send(embed=embed)

async def setup(bot : commands.Bot):
    await bot.add_cog(catfact(bot))
