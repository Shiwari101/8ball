import discord 
from discord.ext import commands
from modules.cactusapi import *

cactus = CactusAPI('VVQuDKHjGfnzRaFLxnHsmdLMZtx4A7XmSPXrZKGD6g2jn')

client = commands.Bot(command_prefix = ".")
class Level(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def level(self, ctx):
        xp = (cactus.userxp(ctx.author.id))
        data = xp
        currentxp = data.split("/")[0]
        nextxp = data.split("/")[1]

        intcurrentxp = int(currentxp)
        intnextxp = int(nextxp)

        print(currentxp)
        print(nextxp)

        level = cactus.userlevel(ctx.author.id)
        intlevel = int(level)
        await ctx.send(f'You are at level {level} with {intcurrentxp} xp. You have to get more {intnextxp - intcurrentxp} xp to get to level {intlevel + 1}')

def setup(client):
    client.add_cog(Level(client))