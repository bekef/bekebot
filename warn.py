from ast import Pass
from msilib.schema import File
from turtle import color
import discord
from discord.ext import commands


class warnsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, Member: discord.Member, reason=None):
        try:
            db = open(f"./cogs/databank/warns/{Member}-warns.txt", "x")
            db()
        except:
            pass
        db = open(f"./cogs/databank/warns/{Member}-warns.txt", "r")
        warnlist = db.read()
        db = open(f"./cogs/databank/warns/{Member}-warns.txt", "w")
        db.write(f"{warnlist}\nTeammitglied: {ctx.author}\n Grund: {reason}\n")
        em001 = discord.Embed(
            title="Verwarnung", description=f"{Member} wurde verwarnt für {reason}", color=0x3498db)
        await ctx.send(embed=em001)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warns(self, ctx, Member: discord.Member):
        db = open(f"./cogs/databank/warns/{Member}-warns.txt", "r")
        warns = db.read()
        em002 = discord.Embed(
            title=f"Verwarnungen von {Member}", description=f"{warns}", color=0x3498db)
        await ctx.send(embed=em002)


def setup(client):
    client.add_cog(warnsys(client))
