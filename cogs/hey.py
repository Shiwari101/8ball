import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '$')


class Hey(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')
    
    @commands.command()
    async def hey(self, ctx):
        await ctx.send(f'Hey how are you {ctx.author.name}?')

        def pred(m):
                return m.author == ctx.author
                
        try: 
            msg = await self.client.wait_for('message', timeout=30.0, check=pred)
        except asyncio.TimeoutError:
            await ctx.send(f'''{ctx.author.name} why you didn't answer me? :c''')
        else: 
            await ctx.send(f'''Ok, if you want to talk about it, you can go to personal vent. it's a safe space''' )



def setup(client):
    client.add_cog(Hey(client))