import discord
import settings
from discord.ext import commands
import requests
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Ready as {bot.user}")
    game = discord.Game(name="nothing :(")
    await bot.change_presence(activity=game)

@bot.command()
async def ping(ctx):
    await ctx.send(f"The Latency Of the bot is {bot.latency}")

@bot.command()
async def avatar(ctx, mention=None):
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

@bot.command()
async def qrcode(ctx, link=None):
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

@bot.command()
async def quotes(ctx):
    response = requests.get("https://zenquotes.io/api/random/")
    response_json = json.loads(response.text) #changes the string json to list json
    response_dict = response_json[0] #acccessing the dict from the list
    response_quote = response_dict['q']
    response_author = response_dict['a']
    embed = discord.Embed(
        description=response_quote
        )
    embed.set_footer(text=f"By {response_author}")
    await ctx.send(embed=embed)

bot.run(settings.DISCORD_TOKEN)
