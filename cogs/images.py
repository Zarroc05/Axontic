import json

import discord
from asyncdagpi import Client, ImageFeatures
from nextcord.ext import commands

with open('./config.json') as f:
    data = json.load(f)
    for c in data['botConfig']:
        api = c['dagpiapi']
dagpi = Client(api)

ecolor = discord.Color.dark_red()


class Images(commands.Cog):
    """Annoy your friends with funny pictures!"""

    def __init__(self, client):
        self.client = client

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def pixel(self, ctx, member: discord.Member = None):
        """Allows you to pixelate a member!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.pixel(), url)
            file = discord.File(fp=img.image, filename=f"pixel.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Pixel")
            embed.set_image(url=f"attachment://pixel.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def colors(self, ctx, member: discord.Member = None):
        """Allows you to get a member with the colors present in the image!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.colors(), url)
            file = discord.File(fp=img.image, filename=f"colors.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Colors")
            embed.set_image(url=f"attachment://colors.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def triggered(self, ctx, member: discord.Member = None):
        """Allows you to get a triggered gif!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.triggered(), url)
            file = discord.File(fp=img.image, filename=f"triggered.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Triggered")
            embed.set_image(url=f"attachment://triggered.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def wasted(self, ctx, member: discord.Member = None):
        """Allows you to get a member with GTA V Wasted Screen!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.wasted(), url)
            file = discord.File(fp=img.image, filename=f"wasted.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Wasted")
            embed.set_image(url=f"attachment://wasted.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def spin(self, ctx, member: discord.Member = None):
        """You spin me right round!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.spin(), url)
            file = discord.File(fp=img.image, filename=f"spin.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Spin")
            embed.set_image(url=f"attachment://spin.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def petpet(self, ctx, member: discord.Member = None):
        """Pet a member!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.petpet(), url)
            file = discord.File(fp=img.image, filename=f"petpet.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="PetPet")
            embed.set_image(url=f"attachment://petpet.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def bonk(self, ctx, member: discord.Member = None):
        """Hit a member with a hammer!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.bonk(), url)
            file = discord.File(fp=img.image, filename=f"bonk.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Bonk")
            embed.set_image(url=f"attachment://bonk.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def bomb(self, ctx, member: discord.Member = None):
        """Explosion!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.bomb(), url)
            file = discord.File(fp=img.image, filename=f"bomb.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Bomb")
            embed.set_image(url=f"attachment://bomb.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def blur(self, ctx, member: discord.Member = None):
        """Blur a specific member!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.blur(), url)
            file = discord.File(fp=img.image, filename=f"blur.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Blur")
            embed.set_image(url=f"attachment://blur.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def delete(self, ctx, member: discord.Member = None):
        """Creates a Windows delete meme based on a specific member!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.delete(), url)
            file = discord.File(fp=img.image, filename=f"delete.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Delete")
            embed.set_image(url=f"attachment://delete.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def lego(self, ctx, member: discord.Member = None):
        """Each group of pixels is a Lego brick!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.lego(), url)
            file = discord.File(fp=img.image, filename=f"lego.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Lego")
            embed.set_image(url=f"attachment://lego.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def wanted(self, ctx, member: discord.Member = None):
        """Wanted poster of a member!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.wanted(), url)
            file = discord.File(fp=img.image, filename=f"wanted.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Wanted")
            embed.set_image(url=f"attachment://wanted.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def mosaic(self, ctx, member: discord.Member = None):
        """Turn a member into a Roman mosaic!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.mosiac(), url)
            file = discord.File(fp=img.image, filename=f"mosaic.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Mosaic")
            embed.set_image(url=f"attachment://mosaic.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def sithlord(self, ctx, member: discord.Member = None):
        """Put a member on the meme "Laughs in Sith Lord"!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.sith(), url)
            file = discord.File(fp=img.image, filename=f"sithlord.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Sith Lord")
            embed.set_image(url=f"attachment://sithlord.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def jail(self, ctx, member: discord.Member = None):
        """Put that member behind bars!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.jail(), url)
            file = discord.File(fp=img.image, filename=f"jail.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Jail")
            embed.set_image(url=f"attachment://jail.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def trash(self, ctx, member: discord.Member = None):
        """The member is trash!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a member!```",
                                          color=ecolor)
                    await ctx.send(embed=embed)
                    return
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.trash(), url)
            file = discord.File(fp=img.image, filename=f"trash.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Trash")
            embed.set_image(url=f"attachment://trash.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def sepia(self, ctx, member: discord.Member = None):
        """Sepia Tone a member!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.sepia(), url)
            file = discord.File(fp=img.image, filename=f"sepia.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Sepia")
            embed.set_image(url=f"attachment://sepia.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def swirl(self, ctx, member: discord.Member = None):
        """Swirl a member!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.swirl(), url)
            file = discord.File(fp=img.image, filename=f"swirl.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Swirl")
            embed.set_image(url=f"attachment://swirl.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def paint(self, ctx, member: discord.Member = None):
        """Turn a member into art!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.paint(), url)
            file = discord.File(fp=img.image, filename=f"paint.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Paint")
            embed.set_image(url=f"attachment://paint.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def magik(self, ctx, member: discord.Member = None):
        """The popular magic ending!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.magik(), url)
            file = discord.File(fp=img.image, filename=f"magik.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Magik")
            embed.set_image(url=f"attachment://magik.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def obama(self, ctx, member: discord.Member = None):
        """The classic meme!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    member = ctx.author
            url = str(member.avatar.with_format("png"))
            img = await dagpi.image_process(ImageFeatures.obama(), url)
            file = discord.File(fp=img.image, filename=f"obama.{img.format}")
            embed = discord.Embed(color=0xa2aac2, title="Obama")
            embed.set_image(url=f"attachment://obama.{img.format}")
            await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def tweet(self, ctx, member: discord.Member = None, *, message=None):
        """Generate a realistic tweet!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a valid member!```",
                                          color=ecolor)
                    await ctx.send(embed=embed)
                    return
                if message is None:
                    embed = discord.Embed(title="❌ Error", description="```fix\nYou have to enter a message!```",
                                          color=ecolor)
                    await ctx.send(embed=embed)
                    return
                url = str(member.avatar.with_format("png"))
                img = await dagpi.image_process(ImageFeatures.tweet(), url, username=member.name, text=message)
                file = discord.File(fp=img.image, filename=f"tweet.{img.format}")
                embed = discord.Embed(color=0xa2aac2, title="Tweet")
                embed.set_image(url=f"attachment://tweet.{img.format}")
                await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def youtube(self, ctx, member: discord.Member = None, *, message=None):
        """Generate a realistic YouTube message!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a valid member!```",
                                          color=ecolor)
                    await ctx.send(embed=embed)
                    return
                if message is None:
                    embed = discord.Embed(title="❌ Error", description="```fix\nYou have to enter a message!```",
                                          color=ecolor)
                    await ctx.send(embed=embed)
                    return
                url = str(member.avatar.with_format("png"))
                img = await dagpi.image_process(ImageFeatures.youtube(), url, username=member.name, text=message,
                                                dark=True)
                file = discord.File(fp=img.image, filename=f"youtube.{img.format}")
                embed = discord.Embed(color=0xa2aac2, title="Youtube")
                embed.set_image(url=f"attachment://youtube.{img.format}")
                await ctx.send(embed=embed, file=file)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def discord(self, ctx, member: discord.Member = None, *, message=None):
        """Generate a realistic Discord message!"""
        if ctx.author.bot is False:
            async with ctx.typing():
                if member is None:
                    embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify a valid member!```",
                                          color=ecolor)
                    await ctx.send(embed=embed)
                    return
                if message is None:
                    embed = discord.Embed(title="❌ Error", description="```fix\nYou have to enter a message!```",
                                          color=ecolor)
                    await ctx.send(embed=embed)
                    return
                url = str(member.avatar.with_format("png"))
                img = await dagpi.image_process(ImageFeatures.discord(), url, username=member.name, text=message,
                                                dark=True)
                file = discord.File(fp=img.image, filename=f"discord.{img.format}")
                embed = discord.Embed(color=0xa2aac2, title="Discord")
                embed.set_image(url=f"attachment://discord.{img.format}")
                await ctx.send(embed=embed, file=file)


########################################################################################################################
def setup(client):
    client.add_cog(Images(client))
