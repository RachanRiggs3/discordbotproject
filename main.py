import discord
import settings
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["!", "."], intents=intents)

def main():

    @bot.event
    async def on_ready():
        print(f"Ready as {bot.user}")
        game = discord.Game(name="with my toys :)")
        await bot.change_presence(activity=game)

    @bot.event
    async def on_ready():
        for files in os.listdir("./commands"):
            if files.endswith(".py"):
                await bot.load_extension(f"commands.{files[:-3]}")

    bot.run(settings.DISCORD_TOKEN)

if __name__ == '__main__':
    main()
