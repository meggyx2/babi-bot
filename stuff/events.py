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
    #assets1 = {large_image:"https://cdn.discordapp.com/attachments/631921445987156021/668410758647775262/141.jpg", large_text:"BOOST BABI"}
    #assets2 = {large_Image:"https://cdn.discordapp.com/avatars/660658512052879401/2f907124939a132235eb342d4978465f.webp?size=1024", large_text:"BOT BY $HIKI"}
    #stream1 = discord.Streaming(name="BOOST BABI", details="Boost Babi for cool perks.", url="discord.gg/babi", game="Boost Babi")
    #stream2 = discord.Streaming(name="BOT BY $HIKI", details="Bot made for the Babi Discord server.", url="https://discord.gg/Qqzy2ds", game="Bot made for the Babi Discord server.")
    #while True:
    #    await bot.change_presence(activity=stream2)
    #    await asyncio.sleep(5)
    #    await bot.change_presence(activity=stream1)
    #    await asyncio.sleep(60)

@bot.event
async def on_message(message):
    ctx = message
    if ctx.channel.id == 633675274675814437:
        chanWLB = bot.get_channel(668462634634575905)
        chanGLB = bot.get_channel(668462870178037771)
        
    
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
    
