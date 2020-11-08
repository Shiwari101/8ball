import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix = '$')


class Minigames(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')
    
    @commands.command()
    async def flip(self,ctx):
        sides = ['Heads', 'Tails']
        await ctx.send(f'Hey {ctx.author.name}! You got {random.choice(sides)}')

    @commands.command()
    async def dice(self, ctx):
        dice = ['1','2','3', '4', '5', '6', '7', '8', '9', '10', '12']
        await ctx.send('You roll a dice and...')
        await asyncio.sleep(5)
        await ctx.send(f'{ctx.author.name}\nYou rolled {random.choice(dice)}')

    @commands.command()
    async def jokenpo(self, ctx):
        hands = ['Rock', 'Paper', 'Scissors']
        await ctx.send(f'{ctx.author.name} Chose {random.choice(hands)}')



def setup(client):
    client.add_cog(Minigames(client))