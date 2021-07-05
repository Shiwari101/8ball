import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions


client = commands.Bot(command_prefix="!", intents=intents)

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ok {self.client.user.name} is Online')
        

    # Ban & Kick
    @commands.command(description="Bans a member")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} was successfully banned!")



    @commands.command(description="Unbans a member")
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        bannedUsers = await ctx.guild.bans()
        name, discriminator = member.split('#')

        for ban in bannedUsers:
            user = ban.user

            if (user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} Was Unbanned")
                return
                    




    # Kick

    @commands.command(description="Kicks a member")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} was kicked successfully!")


    # Lockdown

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lockdown(self, ctx):
        for channel in ctx.guild.channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send('The server is now on lockdown!')



    #unlockdown
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlockdown(self, ctx):
        for channel in ctx.guild.channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send('Server is now unlocked')



    # Mute

    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"Muted {member.mention} for reason {reason}")
        await member.send(f"You were muted in the server {guild.name} for {reason}")




    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await ctx.send(f"Unmuted {member.mention}")
        await member.send(f"You were unmuted in the server {ctx.guild.name}")




def setup(client):
    client.add_cog(Moderation(client))
