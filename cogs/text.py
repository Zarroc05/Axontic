import discord
from discord.ext import commands
from pyfiglet import figlet_format

ecolor = discord.Color.dark_red()


class Text(commands.Cog):
    """Werte deine Texte cool auf!"""

    def __init__(self, client):
        self.client = client

    ####################################################################################################################
    @commands.command(aliases=["upside", "ud"])
    @commands.guild_only()
    async def upsidedown(self, ctx, message=None):
        """Stellt eine Nachricht auf den Kopf!"""
        if ctx.author.bot is False:
            if message is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Nachricht angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            letters = {"?": "¿", "!": "¡", "z": "z", "y": "ʎ", "x": "x", "w": "ʍ", "v": "ʌ", "u": "n", "t": "ʇ",
                       "s": "s", "r": "ɹ", "q": "b", "p": "d", "o": "o", "n": "u", "m": "ɯ", "l": "l", "k": "ʞ",
                       "j": "ɾ",
                       "i": "ı", "h": "ɥ", "g": "ɓ", "f": "ɟ", "e": "ǝ", "d": "p", "c": "ɔ", "b": "q", "a": "ɐ"}
            message = message.lower()
            NewMessage = []
            for letter in message:
                if letter in letters:
                    NewMessage.append(letters[letter])
                else:
                    NewMessage.append(letter)
            await ctx.send("".join(reversed(NewMessage)))

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def sparkle(self, ctx, message=None):
        """Fügt einer Nachricht Glitzer hinzu!"""
        if ctx.author.bot is False:
            if message is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Nachricht angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            letters = {"z": "z͓̽", "y": "y͓̽", "x": "x͓̽", "w": "w͓̽", "v": "v͓̽", "u": "u͓̽", "t": "t͓̽", "s": "s͓̽",
                       "r": "r͓̽", "q": "q͓̽", "p": "p͓̽", "o": "o͓̽", "n": "n͓̽", "m": "m͓̽", "l": "l͓̽", "k": "k͓̽",
                       "j": "j͓̽", "i": "i͓̽", "h": "h͓̽", "g": "g͓̽", "f": "f͓̽", "e": "e͓̽", "d": "d͓̽", "c": "c͓̽",
                       "b": "b͓̽", "a": "a͓̽"}
            message = message.lower()
            NewMessage = ""
            for letter in message:
                if letter in letters:
                    NewMessage += letters[letter]
                else:
                    NewMessage += letter
            await ctx.send(NewMessage)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def fancy(self, ctx, message=None):
        """Macht eine Nachricht schick!"""
        if ctx.author.bot is False:
            if message is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Nachricht angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            letters = {"z": "𝓏", "y": "𝓎", "x": "𝓍", "w": "𝓌", "v": "𝓋", "u": "𝓊", "t": "𝓉", "s": "𝓈", "r": "𝓇",
                       "q": "𝓆", "p": "𝓅", "o": "𝑜", "n": "𝓃", "m": "𝓂", "l": "𝓁", "k": "𝓀", "j": "𝒿", "i": "𝒾",
                       "h": "𝒽",
                       "g": "𝑔", "f": "𝒻", "e": "𝑒", "d": "𝒹", "c": "𝒸", "b": "𝒷", "a": "𝒶"}
            message = message.lower()
            NewMessage = ""
            for letter in message:
                if letter in letters:
                    NewMessage += letters[letter]
                else:
                    NewMessage += letter
            await ctx.send(NewMessage)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def reverse(self, ctx, message=None):
        """Schreibt die Nachricht rückwärts!"""
        if ctx.author.bot is False:
            if message is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Nachricht angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            text_reverse = message[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
            await ctx.send(text_reverse)

    ####################################################################################################################
    @commands.command()
    @commands.guild_only()
    async def big(self, ctx, message=None):
        """Schreibt die Nachricht groß!"""
        if not ctx.author.bot:
            if message is None:
                embed = discord.Embed(title="❌ Fehler", description="```fix\nDu musst eine Nachricht angeben!```",
                                      color=ecolor)
                await ctx.send(embed=embed)
                return
            await ctx.send("```fix\n" + figlet_format(message, font="big") + "```")


########################################################################################################################
def setup(client):
    client.add_cog(Text(client))
