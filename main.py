import discord
import settings
import asyncio
from discord.ext import commands
from os import listdir

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["!", "."], intents=intents)

def main():

    @bot.event
    async def on_ready():
        print(f"Ready as {bot.user}")
        game = discord.Game(name="with my toys :)")
        await bot.change_presence(activity=game)

    async def loading_cogs():
        for files in listdir("./commands"):
            if files.endswith(".py"):
                await bot.load_extension(f"commands.{files[:-3]}")

    asyncio.run(loading_cogs())

    @bot.command()
    @commands.is_owner()
    async def load(ctx, filename: str):
        await bot.load_extension(f"commands.{filename}")
        await ctx.send(f"Loaded {filename} command")
        print(f"Loaded {filename}.py")
    
    @bot.command()
    @commands.is_owner()
    async def unload(ctx, filename: str):
        await bot.unload_extension(f"commands.{filename}")
        await ctx.send(f"Unloaded {filename} command")
        print(f"Unloaded {filename}.py")
    
    @bot.command()
    @commands.is_owner()
    async def reload(ctx, filename : str):
        await bot.reload_extension(f"commands.{filename}")
        await ctx.send(f"Reloaded {filename} command")
        print(f"Reloaded {filename}.py")

    bot.run(settings.DISCORD_TOKEN)

if __name__ == '__main__':
    main()