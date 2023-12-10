import discord
import settings
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Ready as {discord.AppInfo.name}")
    game = discord.Game(name="nothing :(")
    await bot.change_presence(activity=game)

@bot.command()
async def pingme(ctx):
    await ctx.send(f"Pong {ctx.mention}")

bot.run(settings.DISCORD_TOKEN)
