import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image

class wanted(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def wanted(self, ctx, user : discord.Member = None):
        if user == None:
            user = ctx.author
        wanted_image = Image.open(fp=r"C:\Users\HP\Desktop\discord py project\command images\wanted.png")
        user_display_avatar = user.display_avatar
        user_avatar = BytesIO(await user_display_avatar.read())
        pfp = Image.open(user_avatar)  
        
        pfp = pfp.resize((977, 977)) 
        wanted_image.paste(pfp, (217, 453))
        wanted_image.save(fp=r"C:\Users\HP\Desktop\discord py project\command images\command image cache\wanted command cache.png")
        await ctx.send(file=discord.File(fp=r"C:\Users\HP\Desktop\discord py project\command images\command image cache\wanted command cache.png"))

        
async def setup(bot: commands.Bot):
    await bot.add_cog(wanted(bot))