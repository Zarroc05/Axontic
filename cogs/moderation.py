import asyncio
import datetime

import discord
import humanfriendly
from nextcord.ext import commands

prefix = "-"
bc = 0xa2aac2
ecolor = discord.Color.dark_red()


class Moderation(commands.Cog):
    """Take care of law and order!"""

    def __init__(self, client):
        self.client = client
        self.yes = ':white_check_mark:'

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        """Ban a member!"""
        if ctx.author.bot is False:
            time = str(datetime.datetime.now())
            if member is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a member!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if member.top_role >= ctx.author.top_role:
                embed = discord.Embed(title="❌ Error",
                                      description="```fix\nYou can't ban someone who has a higher rank or the same "
                                                  "rank as you!```", color=ecolor)
                await ctx.send(embed=embed)
                return
            else:
                if reason is None:
                    reason = f"No reason given | Banned by {ctx.author}"
                await ctx.guild.ban(member, reason=reason, delete_message_days=0)
                embed = discord.Embed(title=f"**{member}** was banned by: **{ctx.author}**", color=0xa2aac2)
                embed.set_footer(text=f"{member.id} was banned for: {reason}, at: {time[:16]} EST",
                                 icon_url=member.avatar)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id=None):
        """Unban a member!"""
        if ctx.author.bot is False:
            if id is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must provide a member ID!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            ids = (int(id))
            user = await self.client.fetch_user(ids)
            time = str(datetime.datetime.now())
            await ctx.guild.unban(user)
            embed = discord.Embed(title=f"**{user}** has been unbanned by: **{ctx.author}**", color=0xa2aac2)
            embed.set_footer(text=f"{user} was unbanned at: {time[:16]} EST", icon_url=user.avatar)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        """Kick a member from the server!"""
        if ctx.author.bot is False:
            time = str(datetime.datetime.now())
            if member is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a member!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if member.top_role >= ctx.author.top_role:
                embed = discord.Embed(title="❌ You can't kick someone who has a higher rank or the same rank as you!",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            else:
                if reason is None:
                    reason = f"No reason given | Kicked by {ctx.author}"
                await ctx.guild.kick(member, reason=reason)
                embed = discord.Embed(title=f"**{member}** was kicked by: **{ctx.author}**", color=0xa2aac2)
                embed.set_footer(text=f"{member} was kicked for: {reason}, at: {time[:16]} EST",
                                 icon_url=member.avatar)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["clear", "c"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=None):
        """Delete messages!"""
        if ctx.author.bot is False:
            if amount is None:
                amount = 10
            amounts = (int(amount))
            if amounts > 100:
                embed = discord.Embed(title="❌ You can't clean up more than 100 messages!", color=ecolor)
                await ctx.send(embed=embed)
                return
            elif amounts < 1:
                embed = discord.Embed(title="❌ You can't clean up less than 1 message!", color=ecolor)
                await ctx.send(embed=embed)
                return
            deleted = await ctx.channel.purge(limit=(amounts + 1))
            delete = len(deleted)
            embed = discord.Embed(title=f"**{delete - 1}** Messages deleted!", color=0xa2aac2)
            await ctx.send(embed=embed, delete_after=5)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member = None, *, nickname=None):
        """Change the nickname of members!"""
        if member is None:
            embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a member!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if nickname is None:
            embed = discord.Embed(color=bc, title=f"**{member} Nickname successfully reset!**")
            await member.edit(nick=None)
            await ctx.send(embed=embed)
        else:
            if ctx.guild.me.top_role < member.top_role:
                higher_permissions = discord.Embed(
                    title="❌ I can't change the nickname of someone who has a higher rank or the same rank as me!",
                    color=ecolor)
                await ctx.send(embed=higher_permissions)
            elif ctx.author.top_role <= member.top_role:
                user_higher_permissions = discord.Embed(
                    title="❌ You cannot change the nickname of someone who has a higher rank or the same rank as you!",
                    color=ecolor)
                await ctx.send(embed=user_higher_permissions)
            elif ctx.guild.me.top_role > member.top_role:
                embed = discord.Embed(color=bc, title=f"**{member} The nickname was changed to {nickname}!**")
                await member.edit(nick=nickname)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["sm"])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def slowmode(self, ctx, time=None):
        """Set the slowmode in a channel!"""
        if time is None:
            timee = ctx.channel.slowmode_delay
            embed = discord.Embed(title=f'The slowmode in this channel is `{timee}` seconds.', colour=bc)
            await ctx.send(embed=embed)
        else:
            time = humanfriendly.parse_timespan(time)
            if time == 0:
                await ctx.channel.edit(slowmode_delay=0)
                embed = discord.Embed(title=f'{self.yes} Slowmode is set to `None` in this channel.',
                                      colour=bc)
                await ctx.send(embed=embed)
            else:
                await ctx.channel.edit(slowmode_delay=time)
                embed = discord.Embed(
                    title=f'{self.yes} The slowmode in this channel has been changed to `{time}` seconds!',
                    colour=bc)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member = None, time=None, *, reason=None):
        """Mute a member!"""
        if member is None:
            embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a member!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if time is None:
            embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify the time!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if reason is None:
            reason = f"No reason given | Muted by {ctx.author}"
        time = humanfriendly.parse_timespan(time)
        await member.timeout(timeout=discord.utils.utcnow() + datetime.timedelta(seconds=time), reason=reason)
        embed = discord.Embed(title=f"{self.yes} {member} was muted for {round(time)} seconds.\nReason: {reason}",
                              colour=bc)
        await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: discord.Member, reason=None):
        """Unmute a member!"""
        if member is None:
            embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a member!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if reason is None:
            reason = f"No reason given | Unmuted by {ctx.author}"
        await member.remove_timeout(reason=reason)
        embed = discord.Embed(title=f"{self.yes} {member} was unmuted!", colour=bc)
        await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["ar"])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def addrole(self, ctx, role: discord.Role = None, user: discord.Member = None):
        """Add a role to the user(s)!"""
        if role is None:
            embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a role!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if user is None:
            embed = discord.Embed(color=bc, title=f"Add `{role}` to `everyone`!")
            await ctx.send(embed=embed)
            async with ctx.typing():
                for member in ctx.guild.members:
                    await member.add_roles(role)
                embed = discord.Embed(title=f'{self.yes} Successfully added `everyone` the `{role.name}` role!',
                                      colour=bc)
                await ctx.send(embed=embed)
        else:
            await user.add_roles(role)
            embed = discord.Embed(title=f'{self.yes} Successfully added the `{role.name}` role to `{user}`!',
                                  colour=bc)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["rr"])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def removerole(self, ctx, role: discord.Role = None, user: discord.Member = None):
        """Remove a role from the user(s)!"""
        if role is None:
            embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a role!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if user is None:
            embed = discord.Embed(color=bc, title=f"Remove `{role}` from `everyone`.")
            await ctx.send(embed=embed)
            async with ctx.typing():
                for member in ctx.guild.members:
                    await member.remove_roles(role)
                embed = discord.Embed(title=f'{self.yes} Successfully removed the role `{role.name}` from `everyone`!',
                                      colour=bc)
                await ctx.send(embed=embed)
        else:
            await user.remove_roles(role)
            embed = discord.Embed(title=f'{self.yes} Successfully removed the role `{role.name}` from `{user}`!',
                                  colour=bc)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["tc"])
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def tempchannel(self, ctx, name=None, times=None):
        """Create a temporary text channel!"""
        guild = ctx.guild
        channel = await guild.create_text_channel(name=name, category=ctx.channel.category)
        time = humanfriendly.parse_timespan(times)
        embed = discord.Embed(
            description=f'**{self.yes} Successfully created a temporary text channel for `{time}` seconds!**\n'
                        f'**Link: {channel.mention}**', colour=bc)
        await ctx.send(embed=embed)
        await asyncio.sleep(time)
        await channel.delete()
        embed = discord.Embed(title=f"**{self.yes} Successfully deleted temporary text channel!**", colour=bc)
        await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["tv"])
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def tempvoice(self, ctx, name=None, times=None):
        """Create a temporary voice channel!"""
        guild = ctx.guild
        channel = await guild.create_voice_channel(name=name, category=ctx.channel.category)
        time = humanfriendly.parse_timespan(times)
        embed = discord.Embed(
            description=f'**{self.yes} Successfully created a temporary voice channel for `{time}` seconds!**\n'
                        f'**Link: {channel.mention}**', colour=bc)
        await ctx.send(embed=embed)
        await asyncio.sleep(time)
        await channel.delete()
        embed = discord.Embed(title=f"**{self.yes} Successfully deleted temporary voice channel!**", colour=bc)
        await ctx.send(embed=embed)


########################################################################################################################
def setup(client):
    client.add_cog(Moderation(client))
