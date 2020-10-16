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

    def pred(m):
            return m.author == ctx.author
            
    try: 
        msg = await client.wait_for('message', timeout=30.0, check=pred)
    except asyncio.TimeoutError:
        await ctx.send(f'''{ctx.author.name} why you didn't answer me? :c''')
    else: 
        await ctx.send(f'''That's good to know''' )


##commando para ver a latencia 

@client.command()
async def ping(ctx):
    embed = discord.Embed(title = f'''Pong! {round(client.latency * 1000)}ms''', colour = discord.Colour.blue())
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
                'We call Rock Papers Scissors, Jokenpo in Brazil just like in Japan!',
                'Piranha in brazil can be understand as a fish from Amazonas or as a whore/bitch',
                'It is impossible for most people to lick their own elbow. (try it!)',
                'A crocodile cannot stick its tongue out.',
                '''A shrimp's heart is in its head.''',
                'It is physically impossible for pigs to look up into the sky.',
                '''The "sixth sick sheik's sixth sheep's sick" is believed to be the toughest tongue twister in the English language.''',
                'If you sneeze too hard, you could fracture a rib.',
                'Wearing headphones for just an hour could increase the bacteria in your ear by 700 times.',
                'In the course of an average lifetime, while sleeping you might eat around 70 assorted insects and 10 spiders, or more.',
                'Some lipsticks contain fish scales.',
                'Cat urine glows under a black-light.',
                '''Like fingerprints, everyone's tongue print is different.''',
                'Rubber bands last longer when refrigerated.',
                'There are 293 ways to make change for a dollar.',
                '''The average person's left hand does 56% of the typing (when using the proper position of the hands on the keyboard; Hunting and pecking doesn't count!).''',
                'A shark is the only known fish that can blink with both eyes.',
                'The longest one-syllable words in the English language are "scraunched" and "strengthed." Some suggest that "squirreled" could be included, but squirrel is intended to be pronounced as two syllables (squir-rel) according to most dictionaries. "Screeched" and "strengths" are two other long one-syllable words, but they only have 9 letters.',
                '"Dreamt" is the only English word that ends in the letters "mt".',
                'Almonds are a member of the peach family.',
                'Maine is the only state that has a one-syllable name.',
                'There are only four words in the English language which end in "dous": tremendous, horrendous, stupendous, and hazardous.',
                '''Los Angeles' full name is "El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula"''',
                'A cat has 32 muscles in each ear.',
                '''An ostrich's eye is bigger than its brain.''',
                'Tigers have striped skin, not just striped fur.',
                'In many advertisements, the time displayed on a watch is 10:10.',
                '''The characters Bert and Ernie on Sesame Street were named after Bert the cop and Ernie the taxi driver in Frank Capra's "It's a Wonderful Life."''',
                'A dime has 118 ridges around the edge.',
                'The giant squid has the largest eyes in the world.',
                'Most people fall asleep in seven minutes.',
                '"Stewardesses" is the longest word that is typed with only the left hand.']

    embed = discord.Embed(title = 'Fun Fact!', description = f'{random.choice(fun_facts)}', colour = discord.Colour.blue())
                
    await ctx.send(embed = embed)


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
