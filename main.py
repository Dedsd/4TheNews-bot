import nws
import discord
from discord.ext import commands
from datetime import date



token = "TOKEN"

client = commands.Bot(command_prefix="!")

@client.event
async def on_message(message):
    msgcnt = message.content
    cmmnd = msgcnt.startswith("!4news")
    cmmnd2 = msgcnt.startswith("!news_br")
    if cmmnd:
        today = date.today()
        d3 = today.strftime("%m/%d/%y")
        await message.channel.send("**Wait a while until the news are computed**")
        values = nws.newsen()
        embed2 = discord.Embed(
            title=f"",
            description=f'',
            url = f"",
            colour=discord.Colour.dark_blue()
        )
        embed2.add_field(name=f'{values["title111"]}', value=f'[{values["stitle"]}]({values["news1"]})', inline=f'{False}')
        embed2.add_field(name=f'{values["title122"]}', value=f'[{values["stitle1"]}]({values["news2"]})', inline=f'{False}')
        embed2.add_field(name=f'{values["title133"]}', value=f'[{values["stitle2"]}]({values["news3"]})', inline=f'{False}')
        embed2.add_field(name=f"{values['title144']}", value=f'[{values["stitle3"]}]({values["news4"]})', inline=f'{False}')
        embed2.set_footer(text="")
        embed2.set_thumbnail(url='')
        embed2.set_author(name=f"[{d3}] 4TheDay 📰")
        await message.channel.send(embed=embed2)
    if cmmnd2:
        today2 = date.today()
        d4 = today2.strftime("%d/%m/%y")
        await message.channel.send("**Espere até as notícias serem computadas**")
        values2 = nws.newsbr()
        embed3 = discord.Embed(
            title=f"",
            description=f'',
            url = f"",
            colour=discord.Colour.dark_blue()
        )
        embed3.add_field(name=f'{values2["title111br"]}', value=f'[{values2["stitlebr"]}]({values2["news5"]})', inline=f'{False}')
        embed3.add_field(name=f'{values2["title122br"]}', value=f'[{values2["stitle1br"]}]({values2["news6"]})', inline=f'{False}')
        embed3.add_field(name=f'{values2["title133br"]}', value=f'[{values2["stitle2br"]}]({values2["news8"]})', inline=f'{False}')
        embed3.add_field(name=f"{values2['title144br']}", value=f'[{values2["stitle3br"]}]({values2["news9"]})', inline=f'{False}')
        embed3.set_footer(text="")
        embed3.set_thumbnail(url='')
        embed3.set_author(name=f"[{d4}] 4TheDay 📰")
        await message.channel.send(embed=embed3)

        


client.run(token)