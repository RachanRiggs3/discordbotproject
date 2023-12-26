import discord
from discord.ext import commands

class jhelp(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def jhelp(self, ctx):
        embed = discord.Embed(
            title="Help Menu",
            description='''This is a help menu
            !qrcode <link> : this generates a qr image
            !quotes : this generates a random quote
            !catfact : this generates a random cat fact
            !ban <mention> <reason> : bans a user'''
        )
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot : commands.Bot):
    await bot.add_cog(jhelp(bot))