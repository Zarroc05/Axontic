import asyncio
import json

import discord
from nextcord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp

with open('config.json') as f:
    data = json.load(f)
    for c in data['botConfig']:
        token = c['token']
        prefix = c['prefix']

extensions = ['cogs.dev', 'cogs.events', 'cogs.fun', 'cogs.images', 'cogs.info', 'cogs.moderation', 'cogs.text',
              'cogs.utility']

menu = DefaultMenu(active_time=30)
ending_note = "The ending note from Axontic\nFor command {ctx.clean_prefix}{ctx.invoked_with}"

client = commands.Bot(intents=discord.Intents.all(), command_prefix=prefix)

client.help_command = PrettyHelp(menu=menu, ending_note=ending_note, color=0xa2aac2, index_title="Axontic - Help Menu",
                                 no_category="Other Commands", sort_commands=True, show_index=True)


########################################################################################################################
@client.event
async def on_ready():
    print('--------------------------------------')
    print('Axontic is ready!')
    print('Name:', client.user.name)
    print('ID:', client.user.id)
    print('--------------------------------------')
    await status_task()


########################################################################################################################
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name='with Discord!'),
                                     status=discord.Status.do_not_disturb)
        await asyncio.sleep(60)
        await client.change_presence(activity=discord.Game(name='-help | Axontic'),
                                     status=discord.Status.do_not_disturb)
        await asyncio.sleep(60)


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print(f'{extension} could not be loaded. [{error}]')
########################################################################################################################
client.run(token)
