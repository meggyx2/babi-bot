import discord
from discord import Message, Guild, Member
from typing import Optional
from discord.ext import commands

import os
import sys
import traceback
import asyncio
from datetime import datetime
import datetime
import random
import json
import requests

from cv import *

@bot.event
async def on_member_join(member):
    if member.guild.id == 631921445987156019:
        chan = bot.get_channel(663341508954685450)
        await chan.edit(name="babies: {}".format(member.guild.member_count))

@bot.event
async def on_member_remove(member):
    if member.guild.id == 631921445987156019:
        chan = bot.get_channel(663341508954685450)
        await chan.edit(name="babies: {}".format(member.guild.member_count))
    
