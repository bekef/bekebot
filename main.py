import discord
from discord.ext import commands
import os
from apikeys import bottoken

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)


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

client.run(bottoken)