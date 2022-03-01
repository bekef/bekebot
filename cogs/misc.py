import discord
from discord.ext import commands


class misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def toll(self, ctx, user: discord.Member):
        await ctx.send(f"{user.mention}, wow bist du toll")


def setup(client):
    client.add_cog(misc(client))
