import asyncio
import json
import random
import time

import discord
from asyncdagpi import Client
from cowpy import cow
from nextcord.ext import commands

win = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png"
lose = "https://images.emojiterra.com/mozilla/512px/274c.png"
tie = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png"

with open('./config.json') as f:
    data = json.load(f)
    for c in data['botConfig']:
        api = c['dagpiapi']

dagpi = Client(api)
bc = 0xa2aac2
ecolor = discord.Color.dark_red()


########################################################################################################################
def userOnline(memberList):
    online = []
    for i in memberList:
        if not i.bot:
            if i.status == discord.Status.online or discord.Status.idle or discord.Status.dnd:
                online.append(i)
    return online


########################################################################################################################
class Fun(commands.Cog):
    """Have fun on the Discord server!"""

    def __init__(self, client):
        self.client = client

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def cowsay(self, ctx, *, message=None):
        """A cool cow speaks your message!"""
        if ctx.author.bot is False:
            if message is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou have to enter a message!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            moo = cow.Cowacter(thoughts=True)
            msg = moo.milk(msg=message)
            embed = discord.Embed(color=bc, title="Cow 🐮", description=f"Moo! ```{msg}```")
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def penguinsay(self, ctx, *, message=None):
        """A cool penguin speaks your message!"""
        if ctx.author.bot is False:
            if message is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou have to enter a message!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            moo = cow.Tux(thoughts=True)
            msg = moo.milk(msg=message)
            embed = discord.Embed(color=bc, title="Penguin :penguin:", description=f"```{msg}```")
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.group(name="random")
    @commands.guild_only()
    async def random(self, ctx):
        """Shows you the random commands!"""
        if ctx.author.bot is False:
            if ctx.invoked_subcommand is None:
                embed = discord.Embed(title="Random commands", color=bc)
                embed.add_field(name="Choice", value="-random choice [Thing 1, Thing 2, Thing 3]", inline=False)
                embed.add_field(name="User", value="-random user", inline=False)
                embed.add_field(name="Choice", value="-random number [min, max]", inline=False)
                embed.set_footer(text="The elements in '[]' are required, the elements in '()' are optional.",
                                 icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

    ####################################################################################################################
    @random.command()
    @commands.guild_only()
    async def choice(self, ctx, thing1=None, thing2=None, thing3=None):
        if ctx.author.bot is False:
            if thing1 is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify the first argument!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if thing2 is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify the second argument!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if thing3 is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify the third argument!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            choices = (thing1, thing2, thing3)
            time.sleep(1)
            embed = discord.Embed(title=f":tada: Choose between `{thing1}`, `{thing2}` and `{thing3}`", colour=bc)
            msg = await ctx.send(embed=embed)
            time.sleep(2)
            embed1 = discord.Embed(title=f"**.**", colour=bc)
            await msg.edit(embed=embed1)
            time.sleep(0.5)
            embed2 = discord.Embed(title=f"**. .**", colour=bc)
            await msg.edit(embed=embed2)
            time.sleep(0.5)
            embed3 = discord.Embed(title=f"**. . .**", colour=bc)
            await msg.edit(embed=embed3)
            time.sleep(0.5)
            embed4 = discord.Embed(title=f":tada: Choose between `{thing1}`, `{thing2}` and `{thing3}`",
                                   description=f"Pulled: __**{random.choice(choices)}**__", colour=bc)
            await msg.edit(embed=embed4)

    ####################################################################################################################
    @random.command()
    @commands.guild_only()
    async def user(self, ctx):
        if ctx.author.bot is False:
            online = userOnline(ctx.guild.members)
            randomuser = random.choice(online)
            if ctx.channel.permissions_for(ctx.author).mention_everyone:
                user = randomuser
            else:
                user = randomuser
            embed = discord.Embed(title="👥 Choose between `all` users", colour=bc)
            msg = await ctx.send(embed=embed)
            time.sleep(2)
            embed1 = discord.Embed(title=f"**.**", colour=bc)
            await msg.edit(embed=embed1)
            time.sleep(0.5)
            embed2 = discord.Embed(title=f"**. .**", colour=bc)
            await msg.edit(embed=embed2)
            time.sleep(0.5)
            embed3 = discord.Embed(title=f"**. . .**", colour=bc)
            await msg.edit(embed=embed3)
            time.sleep(0.5)
            embed4 = discord.Embed(title=f":tada: Congratulations: __**{user}**__", colour=bc)
            await msg.edit(embed=embed4)

    ####################################################################################################################
    @random.command()
    @commands.guild_only()
    async def number(self, ctx, start=None, end=None):
        if ctx.author.bot is False:
            if start is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify the start value!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            if end is None:
                embed = discord.Embed(title="❌ Error", description="```fix\nYou must specify the end value!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            x = int(start)
            y = int(end)
            embed = discord.Embed(title=f"🔢 Choose between `{x}` - `{y}`", colour=bc)
            msg = await ctx.send(embed=embed)
            time.sleep(2)
            embed1 = discord.Embed(title=f"**.**", colour=bc)
            await msg.edit(embed=embed1)
            time.sleep(0.5)
            embed2 = discord.Embed(title=f"**. .**", colour=bc)
            await msg.edit(embed=embed2)
            time.sleep(0.5)
            embed3 = discord.Embed(title=f"**. . .**", colour=bc)
            await msg.edit(embed=embed3)
            time.sleep(0.5)
            embed4 = discord.Embed(title=f":tada: Choose between `{x}` - `{y}`",
                                   description=f"Pulled: __**{random.randint(x, y)}**__", colour=bc)
            await msg.edit(embed=embed4)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def f(self, ctx, text=None):
        """Show respect to someone or something!"""
        if ctx.author.bot is False:
            if text is None:
                embed = discord.Embed(title="❌ Error",
                                      description="```fix\nYou have to show off something for which you want to show "
                                                  "respect!```", color=ecolor)
                await ctx.send(embed=embed)
                return
            hearts = ["❤", "💛", "💚", "💙", "💜"]
            reason = f"für **{text}**. " if text else ""
            embed = discord.Embed(title=f"__{ctx.author.name}__ shows his respect to {reason}{random.choice(hearts)}",
                                  colour=bc)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def hotcalc(self, ctx, member: discord.Member = None):
        """The bot tells you how hot you are!"""
        if ctx.author.bot is False:
            if member is None:
                member = ctx.author
            random.seed(member.id)
            r = random.randint(1, 100)
            hot = r / 1.17
            if hot > 75:
                emoji = "💞"
            elif hot > 50:
                emoji = "💖"
            elif hot > 25:
                emoji = "❤"
            else:
                emoji = "💔"
            embed = discord.Embed(title=f"**{member.name}** is **{hot:.0f}%** hot {emoji}.", colour=bc)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def slot(self, ctx):
        """Play a little casino to distract yourself!"""
        if ctx.author.bot is False:
            emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
            a = random.choice(emojis)
            b = random.choice(emojis)
            c = random.choice(emojis)
            slotmachine = f"[ {a} | {b} | {c} ]\n"
            embed = discord.Embed(
                title=f"[ {random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)} ]", colour=bc)
            msg = await ctx.send(embed=embed)
            time.sleep(0.5)
            embed1 = discord.Embed(
                title=f"[ {random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)} ]", colour=bc)
            await msg.edit(embed=embed1)
            time.sleep(0.5)
            embed2 = discord.Embed(
                title=f"[ {random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)} ]", colour=bc)
            await msg.edit(embed=embed2)
            time.sleep(0.5)
            embed3 = discord.Embed(
                title=f"[ {random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)} ]", colour=bc)
            await msg.edit(embed=embed3)
            time.sleep(0.5)
            embed4 = discord.Embed(
                title=f"[ {random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)} ]", colour=bc)
            await msg.edit(embed=embed4)
            time.sleep(0.5)
            embed5 = discord.Embed(
                title=f"[ {random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)} ]", colour=bc)
            await msg.edit(embed=embed5)
            if a == b == c:
                embed6 = discord.Embed(title=f"{slotmachine} Everything fits, you win! 🎉", colour=bc)
                await msg.edit(embed=embed6)
            elif (a == b) or (a == c) or (b == c):
                embed7 = discord.Embed(title=f"{slotmachine} 2 in a row, you win! 🎉", colour=bc)
                await msg.edit(embed=embed7)
            else:
                embed8 = discord.Embed(title=f"{slotmachine} No hit, you lost... 😢", colour=bc)
                await msg.edit(embed=embed8)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def flip(self, ctx):
        """Flip a coin!"""
        if ctx.author.bot is False:
            global cancel, headORtail
            try:
                cancel = False
                EmbedHead = discord.Embed(title='Coin toss', color=bc)
                EmbedHead.add_field(name='What is your choice?', value='`head` oder `number`', inline=False)
                EmbedHead.set_thumbnail(
                    url='https://media1.tenor.com/images/38bf85bcecdd6aa52300d53e6eea06a1/tenor.gif')
                EmbedHead.set_footer(text='You have 10 seconds to choose!')
                headORtail = await ctx.send(embed=EmbedHead)
                message = await self.client.wait_for('message', check=lambda
                    m: m.author == ctx.author and m.channel == ctx.channel, timeout=10)
                if str(message.content.lower()) == 'head':
                    user_choose = message.content
                    chooses = ['head', 'number']
                    random_select = random.choice(chooses)
                    if user_choose == random_select:
                        choose_embed = discord.Embed(color=discord.Color.brand_green())
                        choose_embed.add_field(name=':bust_in_silhouette: User', value=f'{user_choose}', inline=True)
                        choose_embed.add_field(name=':robot: Bot', value=f'{random_select}', inline=True)
                        choose_embed.set_author(name='You won', icon_url=win)
                        await ctx.send(embed=choose_embed)
                    else:
                        choose_embed = discord.Embed(color=discord.Color.brand_red())
                        choose_embed.add_field(name=':bust_in_silhouette: User', value=f'{user_choose}', inline=True)
                        choose_embed.add_field(name=':robot: Bot', value=f'{random_select}', inline=True)
                        choose_embed.set_author(name='You lost', icon_url=lose)
                        await ctx.send(embed=choose_embed)
                if str(message.content.lower()) == 'number':
                    user_choose = message.content
                    chooses = ['head', 'number']
                    random_select = random.choice(chooses)
                    if user_choose == random_select:
                        choose_embed = discord.Embed(color=discord.Color.brand_green())
                        choose_embed.add_field(name=':bust_in_silhouette: User', value=f'{user_choose}', inline=True)
                        choose_embed.add_field(name=':robot: Bot', value=f'{random_select}', inline=True)
                        choose_embed.set_author(name='You won', icon_url=win)
                        await ctx.send(embed=choose_embed)
                    else:
                        choose_embed = discord.Embed(color=discord.Color.brand_red())
                        choose_embed.add_field(name=':bust_in_silhouette: User', value=f'{user_choose}', inline=True)
                        choose_embed.add_field(name=':robot: Bot', value=f'{random_select}', inline=True)
                        choose_embed.set_author(name='You lost', icon_url=lose)
                        await ctx.send(embed=choose_embed)
            except asyncio.TimeoutError:
                if not cancel:
                    embed = discord.Embed(title='The time has expired, please try again.', colour=ecolor)
                    await ctx.send(embed=embed)


########################################################################################################################
def setup(client):
    client.add_cog(Fun(client))
