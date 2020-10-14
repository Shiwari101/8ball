import discord
from discord.ext import commands
import random
import os
import asyncio

client = commands.Bot(command_prefix = '.')

##LINKU STARTOO

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.kamihelp'))
    print(f'Ok {client.user.name} is Online')

#.hey é para solitarios como eu que tem seu amigo por um comando

@client.command()
async def hey(ctx):
    await ctx.send(f'Hey how are you {ctx.author.name}?')

##commando para ver a latencia 

@client.command()
async def ping(ctx):
    embed = discord.Embed(title = f'Pong! {round(client.latency * 1000)}ms', colour = discord.Coulor.blue())
    await ctx.send(embed=embed)  

##Comando do 8ball eu vou deixar isso de lado depois no final do dia e vou separar o codigo dele pra estudo

@client.command(aliases = ['8ball', 'kamisama'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.", 
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Questions: {question}\nAnswer: {random.choice(responses)}')

##coin flip roll dice and jokenpo
@client.command()
async def flip(ctx):
    sides = ['Heads', 'Tails']
    await ctx.send(f'Hey {ctx.author.name}! You got {random.choice(sides)}')

@client.command()
async def dice(ctx):
    dice = ['1','2','3', '4', '5', '6', '7', '8', '9', '10', '12']
    await ctx.send('You roll a dice and...')
    await asyncio.sleep(5)
    await ctx.send(f'{ctx.author.name}\nYou rolled {random.choice(dice)}')

@client.command()
async def jokenpo(ctx):
    hands = ['Rock', 'Paper', 'Scissors']
    await ctx.send(f'{ctx.author.name} Chose {random.choice(hands)}')

@client.command()
async def funfact(ctx):
    fun_facts = ['You can send Shiwa some fun facts suggestions, Just DM him ;)',
                'We call Rock Papers Scissors, Jokenpo in Brazil just like in Japan!,'
                'Piranha in brazil can be understand as a fish from Amazonas or as a whore/bitch']
                
    await ctx.send(f'Fun fact: {random.choice(fun_facts)}')


### calculator
@client.command() 
async def add(ctx,a:int,b:int): 
    await ctx.send(f'Ok {a} + {b} = {a+b}')

@client.command() 
async def sub(ctx,a:int,b:int): 
    await ctx.send(f'Ok {a} - {b} = {a-b}')

@client.command() 
async def multiply(ctx,a:int,b:int): 
    await ctx.send(f'Ok {a} X {b} = {a*b}')

@client.command()
async def divide(ctx,a:int,b:int):
    await ctx.send(f'Ok {a} / {b} = {a/b}')


#help command

@client.command()
async def kamihelp(ctx):
    embed = discord.Embed(title = f'Hey {ctx.author.name}. Can I help you?',
                         description = '''Ok... The prefix command is a dot `.` 
and the commands that you can use are `.kamisama` and make your question right after.

You can Flip a coin, Roll a Dice and Play Rock Paper Scissors too.
You can use: `.flip` `.dice` `.jokenpo`

Fun fact we have a fun fact command too! Just type `.funfact` to get one! 
                                            
If you have any question or suggestions you can DM Shiwa. Thanks for using kamisama!''', colour = discord.Colour.blue())
    await ctx.send(embed=embed)



client.run('NzU4MDI3MTQ2ODUyODI3Mzk3.X2o9yw.A9HwTfZKQNLPEMQ7nW1nWX8bzzU')
