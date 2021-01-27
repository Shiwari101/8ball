import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')


class Kamihelp(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')
    
    
    @commands.command()
    async def kamihelp(self, ctx):
        embed = discord.Embed(title = f'Hey {ctx.author.name}. Can I help you?',
                            description = '''Ok... The prefix command is a dot `.` 
    and the commands that you can use are `.kamisama` and make your question right after.

    You can Flip a coin, Roll a Dice and Play Rock Paper Scissors too.
    You can use: `.flip` `.dice` `.jokenpo`

    Fun fact we have a fun fact command too! Just type `.funfact` to get one!

    Kamisama is working on having a integration with Cactus bot.
    So you can use the command `.level` to check your level and how many xp you have left to level up!
                                                
    If you have any question or suggestions you can DM Shiwa. Thanks for using kamisama!''', colour = discord.Colour.blue())
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Kamihelp(client))