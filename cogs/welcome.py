import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')


class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = client.get_guild(692427294261772289)
        channel = guild.get_channel(762347968455508019)

        embed = discord.Embed(title=f"*Welcome to Jimmy's Cult {member}*.",
                              description='''If you want to read the rules again please go to <#692430429017604186>

                                    We have some roles that you can get in <#699319394995535882> with these you can be pinged when we do events for each thing!''', colour=0xFF5F7A)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="*Thanks for joining us and be sure to say hello!*")
        await channel.send("<@&736177693892280420>, say hi to our new member!")
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Welcome(client))
