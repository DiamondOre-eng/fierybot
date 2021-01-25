import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import random


class Giveaways(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Giveaways are now ready!")

    def convert(self, time):
        pos = ["s", "m", "h", "d"]

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gstart(self, ctx):
        await ctx.send("Let's start with this giveaway! Answer these questions within 30 seconds!")

        questions = ["Which channel should it be hosted in?",
                     "What should be the duration of the giveaway? (s|m|h|d)",
                     "What is the prize of the giveaway?"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(i)

            try:
                msg = await self.client.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("You didn't answer in time, please be quicker next time!")
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
            return

        channel = self.client.get_channel(c_id)

        time = self.convert(answers[1])
        if time == -1:
            await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
            return
        elif time == -2:
            await ctx.send(f"The time must be an integer. Please enter an integer next time")
            return

        prize = answers[2]

        await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")

        embed = discord.Embed(title=f"{prize}", description=f"React with :tada: to enter!\nHosted by: {ctx.author.mention}\nEnds {answers[1]} from now", color=discord.Colour.gold())
        g_msg = await channel.send(":tada: **New Giveaway!** :tada:")
        my_msg = await channel.send(embed=embed)

        await my_msg.add_reaction("🎉")
        await asyncio.sleep(time)
        new_msg = await channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        newembed = discord.Embed(title=f"{prize}", description=f"Hosted by: {ctx.author.mention}\nWinner: {winner.mention}", color=discord.Colour.gold())
        await my_msg.edit(embed=newembed)
        await g_msg.edit(content=":tada: **Giveaway Ended!** :tada:")
        await channel.send(f"Congratulations! {winner.mention} won {prize}!")

    @gstart.error
    async def gstart_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Giveaway failed!", color=ctx.author.color)
            embed.add_field(name="Reason:", value="`Administrator Permission is missing!`")
            await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(manage_guild=True)
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("The id was entered incorrectly.\nNext time mention a channel and then the id!")
            return

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        await channel.send(f"Congratulations! The new winner is {winner.mention}.!")

    @reroll.error
    async def reroll_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Reroll failed!", color=ctx.author.color)
            embed.add_field(name="Reason:", value="`Manage Server is missing!`")
            await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(manage_guild=True)
    async def gend(self, ctx, channel: discord.TextChannel, id_: int):
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("The id was entered incorrectly.\nNext time mention a channel and then the id!")
            return

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        await channel.send(f"Congratulations! The winner is {winner.mention}.!")


def setup(client):
    client.add_cog(Giveaways(client))
