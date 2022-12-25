import asyncio
import datetime

import discord
import humanfriendly
from discord.ext import commands

prefix = "-"
bc = 0xa2aac2
ecolor = discord.Color.dark_red()


class Moderation(commands.Cog):
    """Sorge für Recht und Ordnung!"""

    def __init__(self, client):
        self.client = client
        self.yes = ':white_check_mark:'

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        """Banne ein Mitglied!"""
        if ctx.author.bot is False:
            time = str(datetime.datetime.now())
            if member is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst ein Mitglied angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if member.top_role >= ctx.author.top_role:
                embed = discord.Embed(title="❌ Fehler",
                                      description="```fix\nDu kannst keinen bannen, der einen höheren oder denselben "
                                                  "Rang hat wie du!```", color=ecolor)
                await ctx.send(embed=embed)
                return
            else:
                if reason is None:
                    reason = f"Kein Grund angegeben | Gebannt von {ctx.author}"
                await ctx.guild.ban(member, reason=reason, delete_message_days=0)
                embed = discord.Embed(title=f"**{member}** wurde gebannt von: **{ctx.author}**", color=0xa2aac2)
                embed.set_footer(text=f"{member.id} wurde gebannt für: {reason}, Um: {time[:16]} EST",
                                 icon_url=member.avatar)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id=None):
        """Entbanne ein Mitglied!"""
        if ctx.author.bot is False:
            if id is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Mitglied-ID angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            ids = (int(id))
            user = await self.client.fetch_user(ids)
            time = str(datetime.datetime.now())
            await ctx.guild.unban(user)
            embed = discord.Embed(title=f"**{user}** wurde entbannt von: **{ctx.author}**", color=0xa2aac2)
            embed.set_footer(text=f"{user} wurde entbannt um: {time[:16]} EST", icon_url=user.avatar)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        """Schmeiße ein Mitglied vom Server!"""
        if ctx.author.bot is False:
            time = str(datetime.datetime.now())
            if member is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst ein Mitglied angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if member.top_role >= ctx.author.top_role:
                embed = discord.Embed(title="❌ Du kannst keinen kicken, der einen höheren oder denselben Rang hat wie "
                                            "du!", color=ecolor)
                await ctx.send(embed=embed)
                return
            else:
                if reason is None:
                    reason = f"Kein Grund angegeben | Gekickt von {ctx.author}"
                await ctx.guild.kick(member, reason=reason)
                embed = discord.Embed(title=f"**{member}** wurde gekickt von: **{ctx.author}**", color=0xa2aac2)
                embed.set_footer(text=f"{member} wurde gekickt für: {reason}, Um: {time[:16]} EST",
                                 icon_url=member.avatar)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["clear", "c"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=None):
        """Lösche Nachrichten!"""
        if ctx.author.bot is False:
            if amount is None:
                amount = 10
            amounts = (int(amount))
            if amounts > 100:
                embed = discord.Embed(title="❌ Du kannst nicht mehr als 100 Nachrichten bereinigen!", color=ecolor)
                await ctx.send(embed=embed)
                return
            elif amounts < 1:
                embed = discord.Embed(title="❌ Du kannst nicht weniger als 1 Nachricht bereinigen!", color=ecolor)
                await ctx.send(embed=embed)
                return
            deleted = await ctx.channel.purge(limit=(amounts + 1))
            delete = len(deleted)
            embed = discord.Embed(title=f"**{delete - 1}** Nachrichten gelöscht!", color=0xa2aac2)
            await ctx.send(embed=embed, delete_after=5)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member = None, *, nickname=None):
        """Ändere den Nickname von Mitgliedern!"""
        if member is None:
            embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst ein Mitglied angeben!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if nickname is None:
            embed = discord.Embed(color=bc, title=f"**{member} Nickname erfolgreich zurückgesetzt!**")
            await member.edit(nick=None)
            await ctx.send(embed=embed)
        else:
            if ctx.guild.me.top_role < member.top_role:
                higher_permissions = discord.Embed(
                    title="❌ Ich kann den Nickname von jemandem nicht ändern, der einen höheren oder denselben Rang "
                          "hat wie ich!", color=ecolor)
                await ctx.send(embed=higher_permissions)
            elif ctx.author.top_role <= member.top_role:
                user_higher_permissions = discord.Embed(
                    title="❌ Du kannst den Nicknamen von jemandem, der einen höheren oder denselben Rang wie du hat, "
                          "nicht ändern!", color=ecolor)
                await ctx.send(embed=user_higher_permissions)
            elif ctx.guild.me.top_role > member.top_role:
                embed = discord.Embed(color=bc, title=f"**{member} Der Nickname wurde geändert zu {nickname}!**")
                await member.edit(nick=nickname)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["sm"])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def slowmode(self, ctx, time=None):
        """Setze den Slowmode in einem Channel!"""
        if time is None:
            timee = ctx.channel.slowmode_delay
            embed = discord.Embed(title=f'Der Slow-mode in diesem Kanal ist `{timee}` Sekunden.', colour=bc)
            await ctx.send(embed=embed)
        else:
            time = humanfriendly.parse_timespan(time)
            if time == 0:
                await ctx.channel.edit(slowmode_delay=0)
                embed = discord.Embed(title=f'{self.yes} Der Slow-mode ist in diesem Kanal auf `None` gesetzt.',
                                      colour=bc)
                await ctx.send(embed=embed)
            else:
                await ctx.channel.edit(slowmode_delay=time)
                embed = discord.Embed(
                    title=f'{self.yes} Der Slow-Mode in diesem Kanal wurde auf `{time}` Sekunden geändert!',
                    colour=bc)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member = None, time=None, *, reason=None):
        """Mute ein Mitglied!"""
        if member is None:
            embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst ein Mitglied angeben!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if time is None:
            embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst die Zeit angeben!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if reason is None:
            reason = f"Kein Grund angegeben | Gemuted von {ctx.author}"
        time = humanfriendly.parse_timespan(time)
        await member.timeout(until=discord.utils.utcnow() + datetime.timedelta(seconds=time), reason=reason)
        embed = discord.Embed(title=f"{self.yes} {member} wurde gemutet für {round(time)} Sekunden.\nGrund: {reason}",
                              colour=bc)
        await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: discord.Member, reason=None):
        """Entmute ein Mitglied!"""
        if member is None:
            embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst ein Mitglied angeben!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if reason is None:
            reason = f"Kein Grund angegeben | Entmuted von {ctx.author}"
        await member.remove_timeout(reason=reason)
        embed = discord.Embed(title=f"{self.yes} {member} wurde entmuted!", colour=bc)
        await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["ar"])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def addrole(self, ctx, role: discord.Role = None, user: discord.Member = None):
        """Füge dem/den Benutzer(n) eine Rolle zu!"""
        if role is None:
            embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Rolle angeben!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if user is None:
            embed = discord.Embed(color=bc, title=f"Füge `{role}` `everyone` hinzu!")
            await ctx.send(embed=embed)
            async with ctx.typing():
                for member in ctx.guild.members:
                    await member.add_roles(role)
                embed = discord.Embed(title=f'{self.yes} Erfolgreich `everyone` die `{role.name}` Rolle hinzugefügt!',
                                      colour=bc)
                await ctx.send(embed=embed)
        else:
            await user.add_roles(role)
            embed = discord.Embed(title=f'{self.yes} Erfolgreich `{user}` die `{role.name}` Rolle hinzugefügt!',
                                  colour=bc)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["rr"])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def removerole(self, ctx, role: discord.Role = None, user: discord.Member = None):
        """Entferne eine Rolle von dem/den Benutzer(n)!"""
        if role is None:
            embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Rolle angeben!```",
                                  color=ecolor)
            await ctx.send(embed=embed)
            return
        if user is None:
            embed = discord.Embed(color=bc, title=f"Entferne `{role}` von `everyone`")
            await ctx.send(embed=embed)
            async with ctx.typing():
                for member in ctx.guild.members:
                    await member.remove_roles(role)
                embed = discord.Embed(title=f'{self.yes} Erfolgreich `everyone` die Rolle `{role.name}` entfernt!',
                                      colour=bc)
                await ctx.send(embed=embed)
        else:
            await user.remove_roles(role)
            embed = discord.Embed(title=f'{self.yes} Erfolgreich `{user}` die Rolle `{role.name}` entfernt!',
                                  colour=bc)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["tc"])
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def tempchannel(self, ctx, name=None, times=None):
        """Erstelle einen temporären Text Kanal!"""
        guild = ctx.guild
        channel = await guild.create_text_channel(name=name, category=ctx.channel.category)
        time = humanfriendly.parse_timespan(times)
        embed = discord.Embed(
            description=f'**{self.yes} Erfolgreich einen temporären Text Kanal für `{time}` Sekunden erstellt!**\n'
                        f'**Link: {channel.mention}**', colour=bc)
        await ctx.send(embed=embed)
        await asyncio.sleep(time)
        await channel.delete()
        embed = discord.Embed(title=f"**{self.yes} Erfolgreich temporären Text Kanal gelöscht!**", colour=bc)
        await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["tv"])
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def tempvoice(self, ctx, name=None, times=None):
        """Erstelle einen temporären Sprach-Kanal!"""
        guild = ctx.guild
        channel = await guild.create_voice_channel(name=name, category=ctx.channel.category)
        time = humanfriendly.parse_timespan(times)
        embed = discord.Embed(
            description=f'**{self.yes} Erfolgreich einen temporären Sprach-Kanal für `{time}` Sekunden erstellt!**\n'
                        f'**Link: {channel.mention}**', colour=bc)
        await ctx.send(embed=embed)
        await asyncio.sleep(time)
        await channel.delete()
        embed = discord.Embed(title=f"**{self.yes} Erfolgreich temporären Sprach-Kanal gelöscht!**", colour=bc)
        await ctx.send(embed=embed)


########################################################################################################################
def setup(client):
    client.add_cog(Moderation(client))
