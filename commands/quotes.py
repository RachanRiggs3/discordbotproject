import discord
from discord.ext import commands
import requests
import json 

class quotes(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command(aliases=["qs",])
    async def quotes(self, ctx):
        response = requests.get("https://zenquotes.io/api/random/")
        response_json = json.loads(response.text) #changes the string json to list json
        response_dict = response_json[0] #acccessing the dict from the list
        response_quote = response_dict['q']
        response_author = response_dict['a']
        embed = discord.Embed(
            title=response_quote
            )
        embed.set_footer(text=f"By {response_author}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(quotes(bot))