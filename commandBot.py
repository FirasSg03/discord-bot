import discord, os, random
from discord.ext import commands
from dotenv import load_dotenv
import typing


load_dotenv()

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='$')

@bot.command()
async def test(ctx, *args):
    await ctx.send(' '.join(args))

@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send(f'{amount} bottles of {liquid} on the wall!')

@bot.command()
async def jail(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} is going to jail for {reason}')

bot.run(os.getenv('TOKEN'))

"""
https://discordpy.readthedocs.io/en/stable/#getting-started
"""
