import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = '.')

##LINKU STARTOO

@client.event
async def on_ready():
    print(f'Ok {client.user.name} is Online')

#.hey é para solitarios como eu que tem seu amigo por um comando

@client.command()
async def hey(ctx):
    await ctx.send(f'Hey how are you {ctx.author}?')

##commando para ver a latencia é importante mas não vou manter e vou guardar tbm

@client.command()
async def lag(ctx):
    await ctx.send(f'Oh look! {round(client.latency * 1000)}ms')

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

@client.command()
async def kamihelp(ctx):
    await ctx.send(f'''Hey how are you {ctx.author}?
                    So... The prefix command is a dot `.` 
                    and the commands that you can use are `.kamisama` or `.8ball`''')

client.run('NzU4MDI3MTQ2ODUyODI3Mzk3.X2o9yw.A9HwTfZKQNLPEMQ7nW1nWX8bzzU')
