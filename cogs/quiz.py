import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View
import random

class quiz(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="quiz", description="Starte ein Quiz", guild_ids=[954063375535575050])
    async def quiz(self,ctx):
        qcheck = random.randint(1,4)
        if qcheck == 1:
            em001 = discord.Embed(
                title="Quiz",
                description="Wie hoch ist der Mount Everest?",
                color=discord.Color.random()
            )
            em001.set_footer(text="made by Beke")
            em001.set_thumbnail(url="https://img.welt.de/img/wissenschaft/mobile175139769/6402508607-ci102l-w1024/Mount-Everest-Seen-From-The-Air-On-Flight-From-Bhutan-To-Nepal.jpg")

            btn1 = Button(
                label="ca. 4000m",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="ca. 8000m",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            await ctx.respond(embed=em001, view=view)

            async def btn2cb(interaction: discord.Interaction):
                btn2.disabled=True
                await interaction.response.edit_message(embed=em001, view=view)
                await interaction.followup.send("Richtig")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                btn2.disabled=True
                await interaction.response.edit_message(embed=em001, view=view)
                await interaction.followup.send("Falsch")
            btn1.callback = btn1cb

        if qcheck == 2:
            em002 = discord.Embed(
                title="Quiz",
                description="Was ist das Nationaltier Australiens?",
                color=discord.Color.random()
            )
            em002.set_footer(text="made by Beke")
            em002.set_thumbnail(url="https://www.auslandsjob.de/wp-content/uploads/auslandsjob-australien.jpg")
            
            btn1 = Button(
                label="Koala",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="Koyote",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="Rotes Känguru",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            await ctx.respond(embed=em002, view=view)

            async def btn3cb(interaction: discord.Interaction):
                btn3.disabled=True
                await interaction.response.edit_message(embed=em002, view=view)
                await interaction.followup.send("Richtig")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                btn2.disabled=True
                await interaction.response.edit_message(embed=em002, view=view)
                await interaction.followup.send("Falsch")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                btn1.disabled=True
                await interaction.response.edit_message(embed=em002, view=view)
                await interaction.followup.send("Falsch")
            btn1.callback = btn1cb

        if qcheck == 3:
            em003 = discord.Embed(
                title="Quiz",
                description="Wie wurde die Haupstadt der Türkei bis 1923 genannt?",
                color=discord.Color.random()
            )
            em003.set_footer(text="made by Beke")
            em003.set_thumbnail(url="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/54/be/42/hagia-sophia-museum-by.jpg?w=600&h=400&s=1")

            btn1 = Button(
                label="Konstantinopel",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="Ankara",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            await ctx.respond(embed=em003, view=view)

            async def btn2cb(interaction: discord.Interaction):
                btn2.disabled=True
                await interaction.response.edit_message(embed=em003, view=view)
                await interaction.followup.send("Falsch")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                btn1.disabled=True
                await interaction.response.edit_message(embed=em003, view=view)
                await interaction.followup.send("Richtig")
            btn1.callback = btn1cb

        if qcheck == 4:
            em004 = discord.Embed(title="Quiz",description="Wieviele Bundesländer hat Deutschland?",color=discord.Color.random())
            em004.set_footer(text="made by Beke")
            em004.set_thumbnail(url="https://image.geo.de/30104214/t/K5/v3/w1440/r1.7778/-/deutschlandflagge-f-112353939-jpg--57817-.jpg")

            btn1 = Button(
                label="15",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="16",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="17",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            async def btn3cb(interaction: discord.Interaction):
                btn3.disabled=True
                await interaction.response.edit_message(embed=em004, view=view)
                await interaction.followup.send("Falsch")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                btn2.disabled=True
                await interaction.response.edit_message(embed=em004, view=view)
                await interaction.followup.send("Richtig")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                btn1.disabled=True
                await interaction.response.edit_message(embed=em004, view=view)
                await interaction.followup.send("Falsch")
            btn1.callback = btn1cb

            await ctx.respond(embed=em004, view=view)


def setup(client):
    client.add_cog(quiz(client))