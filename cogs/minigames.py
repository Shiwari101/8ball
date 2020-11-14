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
    async def jokenpo(self, ctx, member_1:discord.Member, member_2:discord.Member):

        await member_1.send(f'You started a Jokenpo game, What do you chose?')
        await member_2.send(f'Hey {member_1.name} started a jokenpo game with you {member_2.name}, what you chose?')

        def check(m):
                return m.author == ctx.author

        msg1 = await self.client.wait_for('message', check=check)
            
        def check2(m):
                return m.author == member_2

        msg2 = await self.client.wait_for('message', check=check2)

        print(msg1.content)
        print(msg2.content)
        await ctx.send('Jo!')
        await asyncio.sleep(1)
        await ctx.send('ken!')
        await asyncio.sleep(1)
        await ctx.send('po!')
        await asyncio.sleep(1)
        await ctx.send(f'{member_1.name} choosed {msg1.content} and {member_2.name} {msg2.content}')


def setup(client):
    client.add_cog(Minigames(client))