import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View
import random

class quiz(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="quiz", description="Start a quiz")
    async def quiz(self,ctx):
        qcheck = random.randint(1,4)
        if qcheck == 1:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em001 = discord.Embed(
                title="Quiz",
                description=qn.read(),
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
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em001, view=view)
                    await interaction.followup.send("Right Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em001, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn1.callback = btn1cb

        if qcheck == 2:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em002 = discord.Embed(
                title="Quiz",
                description=qn.read(),
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
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em002, view=view)
                    await interaction.followup.send("Right Answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em002, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em002, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn1.callback = btn1cb

        if qcheck == 3:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em003 = discord.Embed(
                title="Quiz",
                description=qn.read(),
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
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em003, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em003, view=view)
                    await interaction.followup.send("Right Answer")
            btn1.callback = btn1cb

        if qcheck == 4:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em004 = discord.Embed(
                title="Quiz",
                description=qn.read(),
                color=discord.Color.random()
            )
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
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em004, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em004, view=view)
                    await interaction.followup.send("Right Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em004, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn1.callback = btn1cb

            await ctx.respond(embed=em004, view=view)

        if qcheck == 5:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em005 = discord.Embed(
                title="Quiz",
                description=qn.read(),
                color=discord.Color.random()
            )
            em005.set_footer(text="made by Beke")
            em005.set_thumbnail(url="https://media0.faz.net/ppmedia/aktuell/3998753099/1.6813642/default-retina/jetzt-ein-kuehles-bier.jpg")

            btn1 = Button(
                label="ca.50 Litre",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="ca. 20 Litre",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="ca. 100 Litre",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            async def btn3cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em005, view=view)
                    await interaction.followup.send("Right Answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em005, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em005, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn1.callback = btn1cb

            await ctx.respond(embed=em005, view=view)

        if qcheck == 6:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em006 = discord.Embed(
                title="Quiz",
                description=qn.read(),
                color=discord.Color.random()
            )
            em006.set_footer(text="made by Beke")
            em006.set_thumbnail(url="https://cdn-prd.sonnenklar.tv/fileadmin/_processed_/9/5/csm_4t-h-Hawaii-Oahu_600x420_426d838bf2.jpg")

            btn1 = Button(
                label="12",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="62",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="122",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            async def btn3cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em006, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em006, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em006, view=view)
                    await interaction.followup.send("Right Answer")
            btn1.callback = btn1cb

            await ctx.respond(embed=em006, view=view)

        if qcheck == 7:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em007 = discord.Embed(
                title="Quiz",
                description=qn.read(),
                color=discord.Color.random()
            )
            em007.set_footer(text="made by Beke")
            em007.set_thumbnail(url="https://img1.oastatic.com/img2/34448697/900x450r/mount-rushmore.jpg")

            btn1 = Button(
                label="Lincoln",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="Kennedy",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="Washington",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            btn4 = Button(
                label="Roosevelt",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn4)

            async def btn4cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn4.disabled=True
                    await interaction.response.edit_message(embed=em007, view=view)
                    await interaction.followup.send("Right Answer")
            btn4.callback = btn4cb

            async def btn3cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em007, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em007, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em007, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn1.callback = btn1cb

            await ctx.respond(embed=em007, view=view)

        if qcheck == 8:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em008 = discord.Embed(
                title="Quiz",
                description=qn.read(),
                color=discord.Color.random()
            )
            em008.set_footer(text="made by Beke")
            em008.set_thumbnail(url="https://www1.wdr.de/radio/wdr5/sonnenfeuer102~_v-ARDFotogalerie.jpg")

            btn1 = Button(
                label="Earth",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="Pluto",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="Mercur",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            btn4 = Button(
                label="Saturn",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn4)

            async def btn4cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn4.disabled=True
                    await interaction.response.edit_message(embed=em008, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn4.callback = btn4cb

            async def btn3cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em008, view=view)
                    await interaction.followup.send("Right Answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em008, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em008, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn1.callback = btn1cb

            await ctx.respond(embed=em008, view=view)

        if qcheck == 9:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em009 = discord.Embed(
                title="Quiz",
                description=qn.read(),
                color=discord.Color.random()
            )
            em009.set_footer(text="made by Beke")
            em009.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Goethe_%28Stieler_1828%29.jpg/1200px-Goethe_%28Stieler_1828%29.jpg")

            btn1 = Button(
                label="ca.5 years",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="ca.10 years",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="ca. 30 years",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            btn4 = Button(
                label="ca. 60 years",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn4)

            async def btn4cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn4.disabled=True
                    await interaction.response.edit_message(embed=em009, view=view)
                    await interaction.followup.send("Right Answer")
            btn4.callback = btn4cb

            async def btn3cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em009, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em009, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em009, view=view)
                    await interaction.followup.send("Wrong Answer")
            btn1.callback = btn1cb

            await ctx.respond(embed=em009, view=view)

        if qcheck == 10:
            qn = open(f"./cogs/databank/questions/question{qcheck}.txt", "r")
            em010 = discord.Embed(
                title="Quiz",
                description=qn.read(),
                color=discord.Color.random()
            )
            em010.set_footer(text="made by Beke")
            em010.set_thumbnail(url="https://image.stern.de/30407764/t/Ih/v2/w1440/r1.7778/-/schach.jpg")

            btn1 = Button(
                label="ca.20",
                style=discord.ButtonStyle.success,
            )
            view = View()
            view.add_item(btn1)

            btn2 = Button(
                label="ca.30",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn2)

            btn3 = Button(
                label="ca. 15",
                style=discord.ButtonStyle.success,
            )
            view.add_item(btn3)

            async def btn3cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:    
                    btn3.disabled=True
                    await interaction.response.edit_message(embed=em010, view=view)
                    await interaction.followup.send("wrong answer")
            btn3.callback = btn3cb

            async def btn2cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn2.disabled=True
                    await interaction.response.edit_message(embed=em010, view=view)
                    await interaction.followup.send("right answer")
            btn2.callback = btn2cb

            async def btn1cb(interaction: discord.Interaction):
                if interaction.user != ctx.author:
                    await interaction.response.send_message("Start your own Quiz by tiping /Quiz", ephemeral=True)
                else:
                    btn1.disabled=True
                    await interaction.response.edit_message(embed=em010, view=view)
                    await interaction.followup.send("wrong answer")
            btn1.callback = btn1cb

            await ctx.respond(embed=em010, view=view)
          
def setup(client):
    client.add_cog(quiz(client))
