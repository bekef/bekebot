import discord
from discord.ext import commands
import random


class economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['bal', 'Bal'])
    async def balance(self, ctx):
        try:
            balcheck = open(
                f"./cogs/databank/balance/{ctx.author}-bal.txt", "x")
            balcheck()
        except:
            pass
        balcheck = open(f"./cogs/databank/balance/{ctx.author}-bal.txt", "r")
        balcheck.read()
        if balcheck.readline() == " ":
            balcheck = open(
                f"./cogs/databank/balance/{ctx.author}-bal.txt", "r")
            em001 = discord.Embed(
                title=f"Kontostand von {ctx.author}", description=f"Dein Kontostand beträgt:\n  0:coin:", color=0xf1c40f)
            await ctx.send(embed=em001)
        else:
            balcheck = open(
                f"./cogs/databank/balance/{ctx.author}-bal.txt", "r")
            em002 = discord.Embed(
                title=f"Kontostand von {ctx.author}", description=f"Dein Kontostand beträgt:\n {balcheck.readline()} :coin:", color=0xf1c40f)
            await ctx.send(embed=em002)

    @commands.command(aliases=['w', 'Work'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def work(self, ctx):
        try:
            balcheck = open(
                f"./cogs/databank/balance/{ctx.author}-bal.txt", "x")
            balcheck()
        except:
            pass
        rdm = random.randint(0, 1000)
        balcheck = open(f"./cogs/databank/balance/{ctx.author}-bal.txt", "r")
        if balcheck.readline() == "":
            balcheck = open(
                f"./cogs/databank/balance/{ctx.author}-bal.txt", "w")
            balcheck.write("0")
        else:
            pass
        balcheck = open(f"./cogs/databank/balance/{ctx.author}-bal.txt", "r")
        blch = balcheck.read()
        balsum = int(blch) + int(rdm)
        balcheck = open(f"./cogs/databank/balance/{ctx.author}-bal.txt", "w")
        balcheck.write(str(balsum))
        em002 = discord.Embed(
            title="Arbeit beendet", description=f"Du hast gearbeitet und {rdm}:coin: verdient", color=0xf1c40f)
        await ctx.send(embed=em002)


def setup(client):
    client.add_cog(economy(client))
