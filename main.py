import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View
import random
import os
from config import TOKEN

client = commands.Bot(command_prefix=":")

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(
            name="made by Beke", url="https://discord.com/invite/4cRse2E5Yw"
        )
    )
    print("Bot ready to use")


initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)

print(initial_extensions)

client.run(TOKEN)