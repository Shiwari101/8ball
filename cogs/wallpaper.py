import discord
from discord.ext import commands
import praw
import random

client = commands.Bot(command_prefix='$')

reddit = praw.Reddit(client_id='MLf6jAzI7mT-xA',
                     client_secret='DTXfR7NTIfg9alp2deG3UWoPeQXngA',
                     username='Shiwa14',
                     password='Sh1w4r1<\>',
                     user_agent='jtc')


class Wallpaper(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')

    @commands.command()
    async def wallpaper(self, ctx):

        subreddit = reddit.subreddit("wallpaper")
        all_subs = []

        top = subreddit.top_from_week(limit=100)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title=name, colour=discord.Colour.green())
        embed.set_image(url=url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Wallpaper(client))
