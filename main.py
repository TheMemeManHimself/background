import discord
# import asyncio
import os

token = os.environ['TOKEN']

bot = discord.Bot(intents=discord.Intents.all(),)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # while True:
    #     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='A nice game'))
    #     await asyncio.sleep(60)


extensions = [# load cogs
    'cogs.ping',
    'cogs.avatar',
    'cogs.background',
]

if __name__ == '__main__': # import cogs from cogs folder
    for extension in extensions:
        bot.load_extension(extension)
        print(extension)

bot.run(token)  # bot token