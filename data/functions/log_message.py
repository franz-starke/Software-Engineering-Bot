import os
import discord
import datetime

ERROR = 0
INFO = 1
WARNING = 2
SHUTDOWN = 3

RED = 0xff0000
GREEN = 0x00ff00
BLUE = 0x0000ff
YELLOW = 0x00
ORANGE = 0x00
BLACK = 0x000000
WHITE = 0xffffff

COLORMAP = {
    ERROR:RED,
    INFO:BLUE,
    WARNING:YELLOW,
    SHUTDOWN:BLACK
}

async def log_message(method:int,title:str):
    embed = discord.Embed(title=title, color=COLORMAP[method])
    embed.set_footer(text=f'[{str(datetime.datetime.today().strftime("%d.%m.%Y"))} {str(datetime.datetime.today().strftime("%H:%M"))}]')
    await bot.log_text_channel.send(embed=embed)