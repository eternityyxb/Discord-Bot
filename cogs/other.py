from discord.ext import commands
import discord
import datetime

class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.latency = bot.latency

    @commands.command()
    async def ping(self, ctx):
      Ping = str("""```fix\n[ {0}ms ]```""".format(round(self.bot.latency * 1000)))
      embed=discord.Embed(timestamp=datetime.datetime.utcnow(), color=0xFF5733)
      embed.add_field(name="Bot Latency", value=Ping, inline=False)
      embed.set_author(name="Pong", icon_url=self.bot.user.avatar_url)
      embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by: {}".format(ctx.author.display_name))
      await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(other(bot))