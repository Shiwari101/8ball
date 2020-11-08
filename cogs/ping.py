import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '$')


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')
    
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = f'''Pong! {round(self.client.latency * 1000)}ms''', colour = discord.Colour.blue())
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Ping(client))