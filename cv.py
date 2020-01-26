import discord
from discord import Message, Guild, Member
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="*", case_insensitive=True)

lbweek = {}
lbglobal = {}
