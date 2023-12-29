import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO

class twoguys(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def twoguys(self, ctx : commands.Context, user: discord.Member = None):
        if user == None:
            user = ctx.author

        template = Image.open(r"C:\Users\HP\Desktop\discord py project\command images\twoguys.jpg")
        user_avatar = user.display_avatar
        user_avatar = BytesIO(await user_avatar.read())
        user_avatar = Image.open(user_avatar)

        user_avatar = user_avatar.resize((363, 357))
        template.paste(user_avatar, (523, 353))
        template.save(r"C:\Users\HP\Desktop\discord py project\command images\command image cache/two guys command cache.jpg")
        await ctx.send(file=discord.File(r"C:\Users\HP\Desktop\discord py project\command images\command image cache/two guys command cache.jpg"))

async def setup(bot):
    await bot.add_cog(twoguys(bot))