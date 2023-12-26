import discord
from discord.ext import commands

class kick(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx,  error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass required arguments")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions")
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("The bot does not have the required permissions to kick the user")

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member,reason=None):
        await member.kick(reason=reason)

async def setup(bot : commands.Bot):
    await bot.add_cog(kick(bot))