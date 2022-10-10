import os
import discord

from dotenv import load_dotenv
from queries import queries

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    # guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} has logged in to ShoeConverter on CYAccess:\n'
        f'{guild.name} (ID: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to CYS Playground! \n'
        'I am ShoeConverterBot, one of the handful of bots on the server.\n'
        'I can convert your shoe size between US M and W, as well as between international sizes.\n'
        'To get started, simply enter the size you are and the unit you want to convert to in this format:\n'
        '\'<BASE UNIT> <M or W> <SIZE>, and I will retrieve all relevant sizes.\n\n'
        'Available units are: US, UK, EU, IN, CM\n'
        'Available systems are: M (Men/Unisex), W (Women)\n'

    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'help':
        await message.channel.send(
            f'Hi {message.author}, welcome to CYAccess! \n'
            'I am ShoeConverterBot, one of the handful of bots on the server.\n'
            'I can convert your shoe size between US M and W, as well as between international sizes.\n'
            'To get started, simply enter the size you are and the unit you want to convert to in this format:\n'
            '\'<BASE UNIT> <M or W> <SIZE>, and I will retrieve all relevant sizes.\n\n'
            'Available units are: US, UK, EU, IN, CM\n'
            'Available systems are: M, W\n'
            '\n'
            'This feature is currently experimental but is being improved often.'
        )
    else:
        UNITS = ['us', 'uk', 'eu', 'in', 'cm']
        SYSTEMS = ['m', 'w']

        request = message.content.split(" ")
        unit = request[0].lower()
        system = request[1].lower()
        size = request[2]

        if (unit.lower() in UNITS) and (system.lower() in SYSTEMS):
            result = queries.get_sizes(unit, system, size)
            await message.channel.send(result)


# @client.event
# async def on_presence_update():
#


client.run(TOKEN)
