import datetime

import discord
from discord.ext import commands

from util import http

ecolor = discord.Color.dark_red()
bc = 0xa2aac2


########################################################################################################################
def uptime(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, seconds = divmod(r, 60)
    return f"Tage: `{days}` | Stunden: `{hours}` | Minuten: `{minutes}` | Sekunden: `{seconds}`"


########################################################################################################################
async def say_permissions(ctx, member, channel):
    permissions = channel.permissions_for(member)
    e = discord.Embed(color=bc)
    allowed, denied = [], []
    for name, value in permissions:
        name = name.replace('_', ' ').title()
        if value:
            allowed.append(name)
        else:
            denied.append(name)
    e.add_field(name='Erlaubt', value='\n'.join(allowed))
    e.add_field(name='Verweigert', value='\n'.join(denied))
    await ctx.send(embed=e)


########################################################################################################################
class Informationen(commands.Cog):
    """Erhalte neue Informationen!"""

    def __init__(self, client):
        self.client = client
        self.client_start_time = datetime.datetime.now()

    ####################################################################################################################
    @commands.command(aliases=["si"])
    @commands.guild_only()
    async def serverinfo(self, ctx):
        """Hol dir Informationen über den Server!"""
        if ctx.author.bot is False:
            servers = ctx.guild
            embed = discord.Embed(
                title=f"{servers.name}", description=f"{servers.id}", color=0xa2aac2)
            embed.add_field(name="Server Beschreibung:",
                            value=f"> `{servers.description}`", inline=False)
            created_at = str(ctx.guild.created_at)
            embed.add_field(name="Gründungsdatum des Servers:",
                            value=f"> `{created_at[:10]}` um `{created_at[11:16]}`")
            embed.add_field(name="Mitgliederanzahl:",
                            value=f"> `{servers.member_count}` Mitglieder", inline=False)
            RoleCount = 0
            for _ in ctx.guild.roles:
                RoleCount = RoleCount + 1
            embed.add_field(name="Rollenanzahl:",
                            value=f"> `{RoleCount}` Rollen", inline=False)
            embed.add_field(
                name="Emojis Anzahl:", value=f"> `{str(len(servers.emojis))}` Emojis", inline=False)
            TChannelCount = 0
            VChannelCount = 0
            CategoryCount = 0
            for _ in ctx.guild.text_channels:
                TChannelCount = TChannelCount + 1
            for _ in ctx.guild.voice_channels:
                VChannelCount = VChannelCount + 1
            for _ in ctx.guild.categories:
                CategoryCount = CategoryCount + 1
            embed.add_field(name="Anzahl der Kanäle und Kategorien:",
                            value=f"> Kategorien - `{CategoryCount}`,\n> Textkanäle - `{TChannelCount}`,\n> Sprachkan"
                                  f"äle - `{VChannelCount}`", inline=False)
            embed.add_field(name="Server Level",
                            value=f"> `Level {servers.premium_tier}` mit "
                                  f"`{servers.premium_subscription_count} Boosts`.", inline=False)
            embed.set_thumbnail(url=servers.icon)
            embed.set_footer(text=f"Der Server ist im Besitz von: {servers.owner} | {servers.owner.id}",
                             icon_url=servers.owner.avatar)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["ui"])
    @commands.guild_only()
    async def userinfo(self, ctx, member: discord.Member = None):
        """Erhalte Informationen über den Benutzer!"""
        if ctx.author.bot is False:
            if member is None:
                member = ctx.author
            if member.bot:
                message1 = f"`BOT` {member}"
                message2 = f"{member.id}"
            else:
                message1 = f"{member.name}"
                message2 = f"{member.id}"
            embed = discord.Embed(
                title=message1, description=message2, color=bc)
            if member.status is not None:
                embed.add_field(name=f"Status:", value=f"> `{member.status}`")
            else:
                embed.add_field(name=f"Status:", value=f"> `Ich kann den Status des Benutzers nicht abrufen.`",
                                inline=False)
            if member.activity is not None:
                embed.add_field(name=f"Tätigkeit:",
                                value=f"> `{member.activity}`", inline=False)
            else:
                embed.add_field(
                    name=f"Tätigkeit:", value=f"> `Dieser Benutzer spielt nichts.`", inline=False)
            created_at = str(member.created_at)
            embed.add_field(name=f"Datum der Kontoerstellung:", value=f"> `{created_at[:10]}` um `{created_at[11:16]}`",
                            inline=False)
            joined_at = str(member.joined_at)
            embed.add_field(name=f"Datum des Serverbeitritts:", value=f"> `{joined_at[:10]}` um `{joined_at[11:16]}`",
                            inline=False)
            if member.premium_since is not None:
                embed.add_field(name="Booster seit:",
                                value=f"> `{datetime.date.strftime(member.premium_since, '%Y-%m-%d` um `%H:%M')}`",
                                inline=False)
            roles = []
            for role in reversed(member.roles):
                if role.name == "@everyone":
                    roles.append("@everyone")
                else:
                    roles.append(role.mention)
            roles = ", ".join(roles)
            embed.add_field(name="Höchste Rolle:",
                            value=f"> {member.top_role.mention}")
            embed.add_field(name=f"Rollen: ", value=f"> {roles}", inline=False)
            if member.avatar is None:
                embed.set_thumbnail(
                    url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/198142ac-f410-423a-bf0b-34c9cb5d9609/dbtif5j-60306864-d6b7-44b6-a9ff-65e8adcfb911.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE5ODE0MmFjLWY0MTAtNDIzYS1iZjBiLTM0YzljYjVkOTYwOVwvZGJ0aWY1ai02MDMwNjg2NC1kNmI3LTQ0YjYtYTlmZi02NWU4YWRjZmI5MTEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.pRh5DK_cxlZ6SxVPqoUSsSNo1fqksJVP6ECGVUi6kmE")
            if member.avatar is not None:
                embed.set_thumbnail(url=member.avatar)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["ri"])
    @commands.guild_only()
    async def roleinfo(self, ctx, role: discord.Role = None):
        """Erhalte Informationen über die Rolle!"""
        if ctx.author.bot is False:
            if role is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst ein Rolle angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                color=role.color, title=role.name, description=role.id)
            perms = ""
            if role.permissions.administrator:
                perms += "Administrator, "
            if role.permissions.create_instant_invite:
                perms += "Create Instant Invite, "
            if role.permissions.kick_members:
                perms += "Kick Members, "
            if role.permissions.ban_members:
                perms += "Ban Members, "
            if role.permissions.manage_channels:
                perms += "Manage Channels, "
            if role.permissions.manage_guild:
                perms += "Manage Guild, "
            if role.permissions.add_reactions:
                perms += "Add Reactions, "
            if role.permissions.view_audit_log:
                perms += "View Audit Log, "
            if role.permissions.read_messages:
                perms += "Read Messages, "
            if role.permissions.send_messages:
                perms += "Send Messages, "
            if role.permissions.send_tts_messages:
                perms += "Send TTS Messages, "
            if role.permissions.manage_messages:
                perms += "Manage Messages, "
            if role.permissions.embed_links:
                perms += "Embed Links, "
            if role.permissions.attach_files:
                perms += "Attach Files, "
            if role.permissions.read_message_history:
                perms += "Read Message History, "
            if role.permissions.mention_everyone:
                perms += "Mention Everyone, "
            if role.permissions.external_emojis:
                perms += "Use External Emojis, "
            if role.permissions.connect:
                perms += "Connect to Voice, "
            if role.permissions.speak:
                perms += "Speak, "
            if role.permissions.mute_members:
                perms += "Mute Members, "
            if role.permissions.deafen_members:
                perms += "Deafen Members, "
            if role.permissions.move_members:
                perms += "Move Members, "
            if role.permissions.use_voice_activation:
                perms += "Use Voice Activation, "
            if role.permissions.change_nickname:
                perms += "Change Nickname, "
            if role.permissions.manage_nicknames:
                perms += "Manage Nicknames, "
            if role.permissions.manage_roles:
                perms += "Manage Roles, "
            if role.permissions.manage_webhooks:
                perms += "Manage Webhooks, "
            if role.permissions.manage_emojis:
                perms += "Manage Emojis, "
            if perms is None:
                perms = "Keine"
            else:
                perms = perms.strip(", ")
            embed.add_field(name="HEX:", value=f"> {role.colour}")
            embed.add_field(name="RGB:", value=f"> {role.colour.to_rgb()}")
            embed.add_field(name='Anzeigbar', value=f"{str(role.hoist)}")
            embed.add_field(name='Position von unten:',
                            value=f"> {str(role.position)}")
            embed.add_field(name='Verwaltet durch Integration:',
                            value=f"> {str(role.managed)}")
            embed.add_field(name='Erwähnbar:',
                            value=f"> {str(role.mentionable)}")
            embed.add_field(name='Personen in dieser Rolle:',
                            value=f"> {str(len(role.members))}")
            embed.add_field(name='** **', value="** **")
            if role.permissions.value != 0:
                embed.add_field(name='Berechtigungen:',
                                value=f"> {perms}", inline=False)
            else:
                embed.add_field(name='Berechtigungen:',
                                value=f"> Keine", inline=False)
            embed.set_footer(
                text=f"Erstellt: {role.created_at.__format__('%Y-%m-%d at %H:%M')}")
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.group(name="channel")
    @commands.guild_only()
    async def channel(self, ctx):
        """Zeigt dir die Channel-Befehle an!"""
        if ctx.author.bot is False:
            if ctx.invoked_subcommand is None:
                embed = discord.Embed(title="Kanal Befehle", color=bc)
                embed.add_field(
                    name="Text", value="-channel text [#Kanal/Kanal-ID]", inline=False)
                embed.add_field(
                    name="Voice", value="-channel voice [#Voice/Voice-ID]", inline=False)
                embed.add_field(
                    name="Stage", value="-channel stage [#Stage/Stage-ID]", inline=False)
                embed.add_field(
                    name="Category", value="-channel category [Kategorie-ID]", inline=False)
                embed.set_footer(text="Die Elemente in '[]' sind erforderlich, die Elemente in  '()' sind optional.",
                                 icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @channel.command()
    @commands.guild_only()
    async def text(self, ctx, text: discord.TextChannel = None):
        """Erhalte Informationen über den Text-Kanal!"""
        if not ctx.author.bot:
            if text is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst einen Kanal angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            channel_info1 = text.created_at.today().day - text.created_at.day
            embed = discord.Embed(color=bc, title="Text-Kanal")
            embed.add_field(name='Name:', value='> {}'.format(
                text.name), inline=True)
            embed.add_field(name='Kanal-ID:',
                            value='> {}'.format(text.id), inline=True)
            embed.add_field(name='** **', value="** **")
            embed.add_field(name='Typ:', value='> {}'.format(
                text.type), inline=True)
            embed.add_field(name='NSFW:', value='> {}'.format(
                text.is_nsfw()), inline=True)
            embed.add_field(name='** **', value="** **")
            if text.topic is not None:
                embed.add_field(name='Thema:', value='> {}'.format(
                    text.topic), inline=True)
            if text.slowmode_delay > 0:
                embed.add_field(name="Slowmode", value='> {} Sekunden'.format(
                    text.slowmode_delay), inline=True)
                embed.add_field(name='** **', value="** **")
            embed.add_field(name='Erstellt am:', value='> {}'.format(
                "{} (vor {} Tagen!)".format(text.created_at.strftime("%d. %b. %Y %H:%M"), channel_info1)),
                            inline=False)
            embed.set_thumbnail(
                url="https://emoji.gg/assets/emoji/8597-discord-channel-from-vega.png")
            await ctx.send(embed=embed)

    ####################################################################################################################
    @channel.command()
    @commands.guild_only()
    async def voice(self, ctx, voice: discord.VoiceChannel = None):
        """Erhalte Informationen über den Sprach-Kanal!"""
        if not ctx.author.bot:
            if voice is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst einen Voice-Kanal angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            channel_info1 = voice.created_at.today().day - voice.created_at.day
            embed = discord.Embed(color=bc, title="Sprach-Kanal")
            embed.add_field(name='Name:', value='> {}'.format(
                voice.name), inline=True)
            embed.add_field(name='Kanal-ID:',
                            value='> {}'.format(voice.id), inline=True)
            embed.add_field(name='Typ:', value='> {}'.format(
                voice.type), inline=True)
            embed.add_field(name='Bitrate:', value='> {}'.format(
                voice.bitrate), inline=True)
            if voice.user_limit == 0:
                embed.add_field(name='Benutzer-Limit:',
                                value='> Unendlich', inline=True)
            else:
                embed.add_field(
                    name='Benutzer-Limit:', value='> {}'.format(voice.user_limit), inline=True)
            if voice.rtc_region is None:
                embed.add_field(name='** **', value="** **")
            if voice.rtc_region is not None:
                embed.add_field(name='Region:', value='> {}'.format(
                    voice.rtc_region), inline=True)
            embed.add_field(name='Erstellt am:', value='> {}'.format(
                "{} (vor {} Tagen!)".format(voice.created_at.strftime("%d. %b. %Y %H:%M"), channel_info1)),
                            inline=False)
            embed.set_thumbnail(
                url="https://emoji.gg/assets/emoji/6770-discord-voice-from-vega.png")
            await ctx.send(embed=embed)

    ####################################################################################################################
    @channel.command()
    @commands.guild_only()
    async def stage(self, ctx, stage: discord.StageChannel = None):
        """Erhalte Informationen über den Stage-Kanal!"""
        if not ctx.author.bot:
            if stage is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst einen Stage-Kanal angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            channel_info1 = stage.created_at.today().day - stage.created_at.day
            embed = discord.Embed(color=bc, title="Stage-Kanal")
            embed.add_field(name='Name:', value='> {}'.format(
                stage.name), inline=True)
            embed.add_field(name='Kanal-ID:',
                            value='> {}'.format(stage.id), inline=True)
            embed.add_field(name='** **', value="** **")
            embed.add_field(name='Typ:', value='> {}'.format(
                stage.type), inline=True)
            embed.add_field(name='Bitrate:', value='> {}'.format(
                stage.bitrate), inline=True)
            if stage.rtc_region is None:
                embed.add_field(name='** **', value="** **")
            if stage.rtc_region is not None:
                embed.add_field(name='Region:', value='> {}'.format(
                    stage.rtc_region), inline=True)
            embed.add_field(name='Erstellt am:', value='> {}'.format(
                "{} (vor {} Tagen!)".format(stage.created_at.strftime("%d. %b. %Y %H:%M"), channel_info1)),
                            inline=False)
            embed.set_thumbnail(
                url="https://emoji.gg/assets/emoji/9799-stage-channel.png")
            await ctx.send(embed=embed)

    ####################################################################################################################
    @channel.command()
    @commands.guild_only()
    async def category(self, ctx, category: discord.CategoryChannel = None):
        """Erhalte Informationen über die Kategorie!"""
        if not ctx.author.bot:
            if category is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Kategorie angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            channel_info1 = category.created_at.today().day - category.created_at.day
            embed = discord.Embed(color=bc, title="Category")
            embed.add_field(name='Name:', value='> {}'.format(
                category.name), inline=True)
            embed.add_field(name='Kategorie-ID:',
                            value='> {}'.format(category.id), inline=True)
            embed.add_field(name='** **', value="** **")
            embed.add_field(name='Typ:', value='> {}'.format(
                category.type), inline=True)
            embed.add_field(name='NSFW:', value='> {}'.format(
                category.is_nsfw()), inline=True)
            embed.add_field(name='** **', value="** **")
            embed.add_field(name='Erstellt am:', value='> {}'.format(
                "{} (vor {} Tagen!)".format(category.created_at.strftime("%d. %b. %Y %H:%M"), channel_info1)),
                            inline=False)
            embed.set_thumbnail(
                url="https://www.shareicon.net/data/512x512/2016/10/11/842370_multimedia_512x512.png")
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["ei"])
    @commands.guild_only()
    async def emojiinfo(self, ctx, emoji: discord.Emoji = None):
        """Erhalte Informationen über das Emoji!"""
        if not ctx.author.bot:
            if emoji is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst ein Emoji angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
        try:
            emoji = await emoji.guild.fetch_emoji(emoji.id)
        except discord.NotFound:
            embed = discord.Embed(
                title="Ich konnte dieses Emoji auf diesem Server nicht finden!", colour=bc)
            return await ctx.send(embed=embed)
        is_managed = "Ja" if emoji.managed else "Nein"
        is_animated = "Ja" if emoji.animated else "Nein"
        description = f"""
            **__Allgemein:__**
            **- Name:** {emoji.name}
            **- ID:** {emoji.id}
            **- URL:** [Link To Emoji]({emoji.url})
            **- Ersteller:** {emoji.user.mention}
            **- Erstellt am:** {emoji.created_at.strftime("%d. %b. %Y %H:%M")}\n
            **__Anderes:__**
            **- Animiert:** {is_animated}
            **- Verwaltet:** {is_managed}
            **- Server Name:** {emoji.guild.name}
            **- Server ID:** {emoji.guild.id}
            """
        embed = discord.Embed(
            title=f"**Emoji-Informationen für:** `{emoji.name}`", description=description, colour=bc)
        embed.set_thumbnail(url=emoji.url)
        await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def stats(self, ctx):
        """Erhalte die Bot-Statistiken!"""
        if ctx.author.bot is False:
            guildAmt = 0
            guilds = []
            userCount = 0
            up = uptime(datetime.datetime.now() - self.client_start_time)
            for guild in self.client.guilds:
                guildAmt += 1
                userCount += guild.member_count
                guilds.append(f"**{guild.name}**: {guild.member_count}")
            embed = discord.Embed(
                title=f"📊 __**{self.client.user.name} Statistiken**__", color=0xa2aac2)
            embed.add_field(name=f"Bot Ping:",
                            value=f"📶 {round(self.client.latency * 1000)} ms",
                            inline=False)
            embed.add_field(name=f"Bot-Betriebszeit:",
                            value=f"⏰ {up}", inline=False)
            embed.add_field(name=f"Server:",
                            value=f"👾 {guildAmt}", inline=False)
            embed.add_field(name=f"Bots Benutzer:",
                            value=f"🫂 {userCount}", inline=False)
            embed.add_field(name=f"Pycord Version:",
                            value=f"🐍 {discord.__version__}",
                            inline=False)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def covid(self, ctx, country: str = None):
        """Erhalte die aktuellen Corona-Statistiken!"""
        if ctx.author.bot is False:
            if country is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst das Land angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            r = await http.get(f"https://disease.sh/v3/covid-19/countries/{country.lower()}", res_method="json")
            if "message" in r:
                embed = discord.Embed(
                    title="❌ API Fehler", description=f"{r['message']}", color=ecolor)
                await ctx.send(embed=embed)
                return
            json_data = [
                ("Total Cases", r["cases"]), ("Total Deaths", r["deaths"]),
                ("Total Recover", r["recovered"]
                 ), ("Total Active Cases", r["active"]),
                ("Total Critical Condition",
                 r["critical"]), ("New Cases Today", r["todayCases"]),
                ("New Deaths Today", r["todayDeaths"]
                 ), ("New Recovery Today", r["todayRecovered"])
            ]
            embed = discord.Embed(
                description=f"Die bereitgestellten Informationen wurden zuletzt <t:{int(r['updated'] / 1000)}:R> aktualisiert.",
                colour=0xa2aac2)
            for name, value in json_data:
                embed.add_field(name=name, value=f"{value:,}" if isinstance(
                    value, int) else value)
            await ctx.send(
                f"**COVID-19** statistics in :flag_{r['countryInfo']['iso2'].lower()}: **{country.capitalize()}** *({r['countryInfo']['iso3']})*",
                embed=embed)


########################################################################################################################
def setup(client):
    client.add_cog(Informationen(client))
