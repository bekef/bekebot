import discord
from discord.ext import commands
import random


class gamble(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bet(self, ctx):
        pass
    
    @commands.command()
    async def slots(self, ctx):
        pass

def setup(client):
    client.add_cog(gamble(client))