from discord.ext import commands
import aiohttp

class Inspire(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inspire(self, ctx):
      """Get inspiration quotes."""
      async with aiohttp.ClientSession() as session:
            async with session.get("https://api.quotable.io/random") as q:
                    js = await q.json()
                    await ctx.send(f'{js["content"]}\n- {js["author"]}')

    @commands.command()
    async def inspire2(self, ctx):
      """Get anime quotes."""
      async with aiohttp.ClientSession() as session:
            async with session.get("https://animechan.vercel.app/api/random") as q:
                    js = await q.json()
                    await ctx.send(f'{js["quote"]}\n- {js["anime"]}')

def setup(bot):
  bot.add_cog(Inspire(bot))