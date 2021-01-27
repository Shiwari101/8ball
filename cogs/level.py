import discord 
from discord.ext import commands
import random
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

    @commands.command()
    async def predict(self, ctx, member:discord.Member="_"):
        optmist_list = list(range(500, 1000))
        pessimist_list = list(range(100, 300))
        xp = cactus.userxp(ctx.author.id if member == "_" else ctx.author.id)
        xp_month = cactus.usermonthly(ctx.author.id if member == "_" else ctx.author.id)
        data = xp
        currentxp = data.split("/")[0]
        nextxp = data.split("/")[1]

        int_currentxp = int(currentxp)
        int_nextxp = int(nextxp)
        int_xp_month = int(xp_month)
        level = cactus.userlevel(ctx.author.id if member == "_" else ctx.author.id)
        intlevel = int(level)

        ## Ativo (otimista)
        random_optmist_num = random.choice(optmist_list)

        if int_xp_month > 500:
            await ctx.send(f'Hey! You are active. Keep it that way! You earned {int_xp_month} XP this month so far. If you keep that way, you will get {random_optmist_num} XP or even more.')
        else:
            pass

        ## Não ativo (pessimista)
        random_pessimist_num = random.choice(pessimist_list)
        
        if int_xp_month < 500:
            await ctx.send(f'''You are not that active. Try to talk more in  the chat! You've earned only {int_xp_month} so far, If you keep unactive, You might just earn {random_pessimist_num} XP a month. If you gete more active you should get more XP''')
        else:
            pass

        if random_optmist_num >= int_nextxp:
            await ctx.send(f'It looks like you will get level {intlevel + 1}. You have {int_currentxp} XP currently. You have to get more just {int_nextxp - int_currentxp} xp to get level {intlevel + 1}')
        else:
            pass


def setup(client):
    client.add_cog(Level(client))
