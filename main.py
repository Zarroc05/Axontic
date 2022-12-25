import asyncio
import json

import discord
from nextcord.ext import commands
from pretty_help import PrettyHelp

with open('config.json') as f:
    data = json.load(f)
    for c in data['botConfig']:
        token = c['token']
        prefix = c['prefix']

extensions = ['cogs.dev', 'cogs.events', 'cogs.fun', 'cogs.images', 'cogs.info', 'cogs.moderation', 'cogs.text',
              'cogs.utility']

client = commands.Bot(intents=discord.Intents.all(), command_prefix=prefix, help_command=PrettyHelp())


########################################################################################################################
@client.event
async def on_ready():
    print('--------------------------------------')
    print('Genos ist bereit zum Kampf!')
    print('Name:', client.user.name)
    print('ID:', client.user.id)
    print('--------------------------------------')
    await status_task()


########################################################################################################################
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name='with the enemies!'),
                                     status=discord.Status.do_not_disturb)
        await asyncio.sleep(60)
        await client.change_presence(activity=discord.Game(name='-help | Genos'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(60)


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print(f'{extension} konnte nicht geladen werden. [{error}]')
########################################################################################################################
client.run(token)
