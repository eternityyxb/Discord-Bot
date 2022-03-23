import discord
from discord.ext import commands, tasks
from itertools import cycle

class status(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.status = cycle(['With Eternity~'])
        print("cog loaded")

    @tasks.loop(seconds=3.0)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(self.status)))
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        self.change_status.start()

def setup(client):
    client.add_cog(status(client))