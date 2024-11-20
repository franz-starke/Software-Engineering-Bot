#!/usr/bin/python3

#----------------------------------------------------
# This is a discord bot to manage a Software-Engineering Project Version 1.0.1
# Created by gamexdifficulty
# Programmed in Python 3.13.0
# This code is licensed under GPLv3s
#----------------------------------------------------

import discord
from data.classes.events import *
from data.functions.log import *

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        self.guild_id = 1298261653191659554
        
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await slash.sync(guild=discord.Object(id=self.guild_id))
            self.synced = True

        self.guild = await self.fetch_guild(self.guild_id)
        self.general_text_channel = await self.guild.fetch_channel(1298261653191659557)
        self.announcement_text_channel = await self.guild.fetch_channel(1298261653191659557)
        self.member_role = self.guild.get_role(1298261895358316544)

        self.events = Events(self)

        log(INFO,"SE-Bot online.")
        self.event_updater = self.loop.create_task(self.events.update())

if __name__ == "__main__":
    try:
        token = ""
        bot = Bot()
        slash = discord.app_commands.CommandTree(bot)
        bot.run(token)
    except Exception as e:
        log(ERROR,f"Failed to start: {e}")