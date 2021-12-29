import discord
import random
from discord.ext import commands

from apikeys import *

client = commands.Bot(command_prefix = "!")


#when bot is online
@client.event
async def on_ready():
    print("Bekebot is online")


#clear
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"Es wurden {amount} Nachrichten gelöscht")


#kick
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send (f"{member.mention} wurde gekickt \n Grund: {reason}")


#ban
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send (f"{member.mention} wurde gebannt \n Grund: {reason}")


#unban
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    
    for ban_entry in banned_users:
        user=ban_entry.user

        if(user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} wurde entbannt")
            return


#checks for specific messages      
@client.event
async def on_message(message):
    if message.content == "hilfe":
        await message.channel.send(f"Es wurde ein Mod wurde benachrichtigt")

client.run(BOTTOKEN)    