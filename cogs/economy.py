import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View
import random

class ecosys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="work", description="go work", guild_ids=[954063375535575050])
    @commands.cooldown(1,3600,commands.BucketType.user)
    async def work(self,ctx):
        try:
            balcheck = open(
                f"./cogs/databank/economy/{ctx.author}-bal.txt", "x")
            balcheck()
        except:
            pass
        rdm = random.randint(0, 1000)
        balcheck = open(f"./cogs/databank/economy/{ctx.author}-bal.txt", "r")
        if balcheck.readline() == "":
            balcheck = open(
                f"./cogs/databank/economy/{ctx.author}-bal.txt", "w")
            balcheck.write("0")
        else:
            pass
        balcheck = open(f"./cogs/databank/economy/{ctx.author}-bal.txt", "r")
        blch = balcheck.read()
        balsum = int(blch) + int(rdm)
        balcheck = open(f"./cogs/databank/economy/{ctx.author}-bal.txt", "w")
        balcheck.write(str(balsum))
        em001 = discord.Embed(
            title="Arbeit beendet", 
            description=f"You worked and got {rdm}:coin:", 
            color=discord.Color.gold()
            )
        await ctx.respond(embed=em001)

    @commands.slash_command(name="balance", description="check your balance", guild_ids=[954063375535575050])
    async def bal(self,ctx):
        try:
            balcheck = open(
                f"./cogs/databank/economy/{ctx.author}-bal.txt", "x")
            balcheck()
        except:
            pass
        balcheck = open(f"./cogs/databank/economy/{ctx.author}-bal.txt", "r")
        balcheck.read()
        if balcheck.readline() == " ":
            balcheck = open(
                f"./cogs/databank/economy/{ctx.author}-bal.txt", "r")
            em001 = discord.Embed(
                title=f"Kontostand von {ctx.author}",
                description=f"Dein Kontostand beträgt:\n  0:coin:", 
                color=discord.Color.gold()
                )
            await ctx.respond(embed=em001)
        else:
            balcheck = open(
                f"./cogs/databank/economy/{ctx.author}-bal.txt", "r")
            em002 = discord.Embed(
                title=f"Kontostand von {ctx.author}", 
                description=f"Dein Kontostand beträgt:\n {balcheck.readline()} :coin:", 
                color=discord.Color.gold()
                )
            await ctx.respond(embed=em002)

def setup(client):
    client.add_cog(ecosys(client))