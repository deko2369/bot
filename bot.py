import discord
from discord.ext import commands
from pytz import timezone
from print_ctf import ctf_info

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ctf(ctx):
    info = ctf_info(tz=timezone('Asia/Tokyo'))
    await ctx.send(info)

bot.run('token')