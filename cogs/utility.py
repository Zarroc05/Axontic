import random
from string import ascii_letters
from string import digits
from string import punctuation

import discord
from nextcord.ext import commands

bc = 0xa2aac2
ecolor = discord.Color.dark_red()


class General(commands.Cog):
    """Standard commands for everyone!"""

    def __init__(self, client):
        self.client = client

    ####################################################################################################################
    @commands.command(aliases=["a"])
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member = None):
        """Get the member avatar!"""
        if ctx.author.bot is False:
            if member is None:
                member = ctx.author
            if member.avatar is None:
                embed = discord.Embed(title=f"**__{member}'s Avatar__**", color=0xa2aac2)
                embed.set_thumbnail(
                    url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/198142ac-f410-423a-bf0b-34c9cb5d9609/dbtif5j-60306864-d6b7-44b6-a9ff-65e8adcfb911.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE5ODE0MmFjLWY0MTAtNDIzYS1iZjBiLTM0YzljYjVkOTYwOVwvZGJ0aWY1ai02MDMwNjg2NC1kNmI3LTQ0YjYtYTlmZi02NWU4YWRjZmI5MTEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.pRh5DK_cxlZ6SxVPqoUSsSNo1fqksJVP6ECGVUi6kmE")
                await ctx.send(embed=embed)
            if member.avatar is not None:
                embed = discord.Embed(title=f"**__{member}'s Avatar__**",
                                      description=f"> [Avatar Link (PNG)]({member.avatar.with_format('png')})\n> [Avatar "
                                                  f"Link (JPG)]({member.avatar.with_format('jpg')})\n> [Avatar L"
                                                  f"ink (WebP)]({member.avatar.with_format('webp')})",
                                      color=0xa2aac2)
                embed.set_image(url=member.avatar.with_format("png"))
                await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, channel: discord.TextChannel = None, message=None):
        """Create a short survey!"""
        if ctx.author.bot is False:
            if channel is None:
                embed = discord.Embed(title="??? Error",
                                      description="```fix\nYou must specify a channel!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if message is None:
                embed = discord.Embed(title="??? Error",
                                      description="```fix\nYou have to enter a question!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(title="Done", colour=bc)
            await ctx.send(embed=embed)
            sender = ctx.author.name
            embed = discord.Embed(title="???? Survey", colour=0xa2aac2)
            embed.add_field(name="Question", value=message, inline=False)
            embed.set_footer(text=f"Survey by {sender}")
            msg = await channel.send(embed=embed)
            await msg.add_reaction("????")
            await msg.add_reaction("????")

    ####################################################################################################################
    @commands.command(aliases=["pw"])
    @commands.guild_only()
    async def password(self, ctx, length: int = None):
        """Generate a password via DM!"""
        if ctx.author.bot is False:
            if length is None:
                embed = discord.Embed(title="??? Error",
                                      description="```fix\nYou must specify a character length!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            password = '' ''
            symbol = ascii_letters + digits + punctuation
            secure_random = random.SystemRandom()
            if length <= 7:
                embed = discord.Embed(title="??? This password is not secure.\nBetter take one with 8 letters!",
                                      colour=ecolor)
                await ctx.send(embed=embed)
            else:
                for i in range(length):
                    password += "".join(secure_random.choice(symbol))
                embed = discord.Embed(color=bc, title="Secure password", description=f"`{password}`")
                await ctx.author.send(embed=embed)
                embed = discord.Embed(title="Check your DMs :)", colour=bc)
                await ctx.send(embed=embed)


########################################################################################################################
def setup(client):
    client.add_cog(General(client))
