import discord
from discord.ext import commands

extensions = ['kamisama', 'funfact', 'minigames', 'hey', 'ping', 'kamihelp',]

client = commands.Bot(command_prefix = '.')

##LINKU STARTOO

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.kamihelp'))
    for ext in extensions:
        client.load_extension(f'cogs.{ext}')
        print(f"[EXTENSION] {ext} is now running...")
    print(f'Ok {client.user.name} is Online')


client.run('NzU4MDI3MTQ2ODUyODI3Mzk3.X2o9yw.A9HwTfZKQNLPEMQ7nW1nWX8bzzU')
