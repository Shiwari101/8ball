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
        embed = discord.Embed(title = f'Hey {ctx.author.name}. How can I help you?',
                            description = '''Ok let's start... The prefix command is `k.` 
    and the commands that you can use are:
    You can use `k.kamisama (Your question)` to make a question.

    You can Flip a coin, Roll a Dice and Play Rock Paper Scissors too.
    You can use: `k.flip` `k.dice` `k.jokenpo`

    Kamisama has a Fun fact command too! Just type `k.funfact` to get one!
    If you want a new wallpaper, use `k.wallapaper`
    

    Kamisama is working on having a integration with Cactus bot.

    So you can use the command `k.level` to check your level and how many xp you have left to level up!
    
    Also `k.predict` to predict your level! (This is the alpha stage of this feature. so this will not be accurate)
                                                
    If you have any question or suggestions you can DM Shiwa. Thanks for using kamisama!''', colour = discord.Colour.purple())
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Kamihelp(client))