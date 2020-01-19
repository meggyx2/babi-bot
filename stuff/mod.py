import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
import datetime
import json

from datetime import datetime

from cv import *

@bot.command(aliases=["botclear", "botclean", "clean", "clear", "fuckoffbots", "botclear", "botclean"])
@commands.has_permissions(manage_messages=True)
async def bc(ctx):
    def check(m):
        return m.author.bot
    ctx.message.delete()
    await ctx.message.channel.purge(limit=100, check=check)
