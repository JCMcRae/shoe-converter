import discord

client = discord.Client()


@client.event
async def on_ready():
    print('You are logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startsWith('$hello'):
        await message.channel.send('Hello!')

client.run('Your token is here')
