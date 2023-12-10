import discord
import settings
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Ready as {bot.user}")
    game = discord.Game(name="nothing :(")
    await bot.change_presence(activity=game)

@bot.command()
async def pingme(ctx):
    await ctx.send(f"Pong {ctx.author.mention}")

@bot.command()
async def avatar(ctx, mention=None):
    if not mention: 
        useravatarurl = ctx.author.avatar
        await ctx.send(useravatarurl)
    else:
        user = ctx.message.mentions[0] 
        useravatarurl = user.avatar
        await ctx.send(useravatarurl)

bot.run(settings.DISCORD_TOKEN)
