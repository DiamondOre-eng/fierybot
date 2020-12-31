import discord
from discord.ext import commands
from discord.ext.commands import Bot, bot

client = Bot(command_prefix='?')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Watching over Fiery Warriors"))
    print('Bot is ready!')

client.run("Nzk0MjM3Mzc1Nzg5NTMxMTY3.X-35Mg.ERIQpJ-iYsqFQNBl2rycP2jfK94")
