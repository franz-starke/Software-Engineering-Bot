import discord
import datetime

from main import Bot
from data.classes.events import Event
from data.functions.log import *

class ReminderEvent(Event):
    def __init__(self, bot:Bot) -> None:
        super().__init__(bot)
        self.prepared = False

    async def check_event_time(self):

        # Check if weekday is sunday
        if datetime.datetime.now().date().weekday() == 6:

            # Check time
            if datetime.datetime.now().hour == 12 and datetime.datetime.now().minute == 0:
                return True
            
        return await super().check_event_time()
    
    async def prepare(self):
        self.prepared = True

    async def start(self):
        await super().start()

        # Send reminder
        embed = discord.Embed(color=0xfa5c07,title="***Erinnerung an alle: Protokoll letzter Woche noch einmal anschauen.***")
        await self.bot.general_text_channel.send(self.bot.member_role,embed=embed)

    async def update(self):
        return True

    async def end(self):
        await super().end()
        self.prepared = False