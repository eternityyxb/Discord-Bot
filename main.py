import os
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()
bot = commands.Bot(command_prefix='$')

bot.load_extension("cogs.maincog")
bot.load_extension("cogs.music")
bot.load_extension("cogs.statuscog")
bot.load_extension("cogs.inspirecog")
bot.load_extension("cogs.other")

keep_alive()

bot.run(os.getenv('TOKEN'))