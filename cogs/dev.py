import discord
from nextcord.ext import commands

bc = 0xa2aac2
ecolor = discord.Color.dark_red()


class Developer(commands.Cog):
    """Commands for the owner!"""

    def __init__(self, client):
        self.client = client

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def servers(self, ctx):
        """Sends all servers!"""
        if ctx.author.bot is False:
            servers = list(self.client.guilds)
            embed = discord.Embed(title="**Connected to {0} servers:**".format(str(len(servers))), colour=bc)
            for server in servers:
                embed.add_field(name=server.name, value=server.id, inline=False)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def leave(self, ctx, serverid: discord.Guild = None):
        """Force the bot to leave a server!"""
        if ctx.author.bot:
            pass
        if not ctx.author.bot:
            if serverid is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a server ID!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            embed2 = discord.Embed(title="Exit", description=f"I have left the server `{serverid.name}`.",
                                   colour=bc)
            await ctx.send(embed=embed2)
            await serverid.leave()


########################################################################################################################
def setup(client):
    client.add_cog(Developer(client))
