import discord
from discord.ext import commands
from modules.cactusapi import *

cactus = CactusAPI("9RJWwx2emnj9pRrjXUzpaTByBLYvazrzjftYw3UHgmZKR")

class Owoapi(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(762359461250727997)
        owo_level = cactus.userlevel(717747572076314745)

        if owo_level == '40':
            await channel.send('this message was only possible with Cactus API made by: owoqq <3')
        else:
            return

def setup(client):
    client.add_cog(Owoapi(client))
    

