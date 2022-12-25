import discord
from discord.ext import commands

ecolor = discord.Color.dark_red()


class Events(commands.Cog):
    """Automatisierte Events für den Bot!"""

    def __init__(self, client):
        self.client = client

    ####################################################################################################################
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title="❌ Fehler", color=ecolor)
        embed.add_field(name='Fehler:', value="```python\n{}```".format(error), inline=False)
        embed.set_thumbnail(url=self.client.user.avatar)
        await ctx.send(embed=embed)


########################################################################################################################
def setup(client):
    client.add_cog(Events(client))
