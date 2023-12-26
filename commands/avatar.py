import discord
from discord.ext import commands

class avatar(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def avatar(self, ctx, mention=None):
        if mention==None: 
            embed = discord.Embed(
                title=f"{ctx.author}'s Avatar",
                description="below is the avatar",
                color=discord.Color.blurple()
            )
            avatar_link = ctx.author.avatar.url
            embed.set_image(url=avatar_link)
            await ctx.send(embed=embed)
        else:
            user = ctx.message.mentions[0]
            embed = discord.Embed(
                title=f"{user}'s Avatar",
                description="below is the avatar",
                color=discord.Color.blurple()
            )
            useravatarurl = user.avatar.url
            embed.set_image(url=useravatarurl)
            await ctx.send(embed=embed)

async def setup(bot : commands.Bot=None):
    await bot.add_cog(avatar(bot))