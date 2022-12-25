import discord
from discord.ext import commands

bc = 0xa2aac2
ecolor = discord.Color.dark_red()


class Entwickler(commands.Cog):
    """Befehle für den Inhaber!"""

    def __init__(self, client):
        self.client = client

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def servers(self, ctx):
        """Sendet alle Server!"""
        if ctx.author.bot is False:
            servers = list(self.client.guilds)
            embed = discord.Embed(title="**Verbunden mit {0} Servern:**".format(str(len(servers))), colour=bc)
            for server in servers:
                embed.add_field(name=server.name, value=server.id, inline=False)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command(aliases=["r"])
    @commands.guild_only()
    @commands.is_owner()
    async def reboot(self, ctx):
        """Startet den Bot neu!"""
        if ctx.author.bot is False:
            embed = discord.Embed(title="Egal was! Was auch immer notwendig ist.", colour=bc)
            await ctx.send(embed=embed)
            await self.client.close()

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def leave(self, ctx, serverid: discord.Guild = None):
        """Zwinge den Bot einen Server zu verlassen!"""
        if ctx.author.bot:
            pass
        if not ctx.author.bot:
            if serverid is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Server ID angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            embed2 = discord.Embed(title="Verlassen", description=f"Ich habe den Server `{serverid.name}` verlassen.",
                                   colour=bc)
            await ctx.send(embed=embed2)
            await serverid.leave()


########################################################################################################################
def setup(client):
    client.add_cog(Entwickler(client))
