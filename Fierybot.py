import discord
from discord.ext import commands
from discord.ext.commands import Bot, bot

client = Bot(command_prefix=':')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Watching over Fiery Warriors"))
    print('Bot is ready!')

CHANNEL_ID = 794243325817257984


@client.command()
async def suggest(ctx, *, description):
    embed = discord.Embed(title='New suggestion!', description=f'Suggested by: {ctx.author.mention}', color=discord.Color.green())
    embed.add_field(name='Description', value=description)
    channel = ctx.guild.get_channel(CHANNEL_ID)
    msg = await channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await ctx.send("Successfully sent your suggestion!")

client.load_extension("giveaways")
    
client.run("Nzk0MjM3Mzc1Nzg5NTMxMTY3.X-35Mg.JSrKaA6zIuvIjBQ60hOImwLHDmQ")
