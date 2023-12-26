import discord 
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx,  error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass required arguments")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions")
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("The bot does not have the required permissions to ban the user")

    @commands.command(aliases=["b",])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, reason=None):
        await member.ban(reason=reason)

async def setup(bot : commands.Bot=None):
    await bot.add_cog(ban(bot))

    