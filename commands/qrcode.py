import discord
from discord.ext import commands

class qrcode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["qr",])
    async def qrcode(self, ctx, link=None):
        if link == None:
            await ctx.send("Please add a link")
        else:
            embed = discord.Embed(
                title="QR Code",
                description="QR Code is generated",
                color=discord.Colour.blue()
            )
            embed.set_image(url=f'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={link}')
            await ctx.send(embed=embed)

async def setup(bot : commands.Bot):
    await bot.add_cog(qrcode(bot))