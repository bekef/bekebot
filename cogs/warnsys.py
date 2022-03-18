import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View
import random

class warnsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="warn", description="warn a User", guild_ids=[954063375535575050])
    @commands.has_permissions(kick_members = True)
    async def warn(self,ctx,member:discord.Member,reason):
        try:
            db = open(f"./cogs/databank/warns/{member}-warns.txt", "x")
            db()
        except:
            pass
        db = open(f"./cogs/databank/warns/{member}-warns.txt", "r")
        warnlist = db.read()
        db = open(f"./cogs/databank/warns/{member}-warns.txt", "w")
        db.write(f"{warnlist}\nStaffmember: {ctx.author}\n Reason: {reason}\n")
        await ctx.respond("Verwarnung erfolgreich", ephemeral=True)

    @commands.slash_command(name="warns", description="Look at the Warnings of a Member", guild_ids=[954063375535575050])
    @commands.has_permissions(kick_members = True)
    async def warns(self,ctx,member:discord.Member):
        try:
            db = open(f"./cogs/databank/warns/{member}-warns.txt", "x")
            db()
        except:
            pass
        db = open(f"./cogs/databank/warns/{member}-warns.txt", "r")
        warns = db.readline()
        db.readline()
        em002 = discord.Embed(
            title=f"Warnings of {member.mention}", 
            description=f"Warnings:\n{warns}", 
            color=discord.Color.red())
        em002.set_footer(text="made by Beke")
        await ctx.respond(embed=em002)

def setup(client):
    client.add_cog(warnsys(client))