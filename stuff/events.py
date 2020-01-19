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
async def on_ready():
    print("meg eww")
    stream1 = discord.Streaming(name="BOOST BABI", details="Boost Babi for cool perks.", url="discord.gg/babi")
    stream2 = discord.Streaming(name="BOT BY $HIKI", details="Bot made for the Babi Discord server.", url="https://discord.gg/Qqzy2ds")
    while True:
        await bot.change_presence(activity=stream1)
        await asyncio.sleep(20)
        await bot.change_presence(activity=stream2)
        await asyncio.sleep(10)

@bot.event
async def on_member_join(member):
    if member.guild.id == 631921445987156019:
        chan = bot.get_channel(665508950996680705)
        await chan.edit(name="babies: {}".format(member.guild.member_count))

@bot.event
async def on_member_remove(member):
    if member.guild.id == 631921445987156019:
        chan = bot.get_channel(665508950996680705)
        await chan.edit(name="babies: {}".format(member.guild.member_count))
    
