from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

import os
import discord
import asyncio

from utils.profile import get_profile
from utils.score import get_score

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "?", intents = intents, help_command = None)

@bot.event
async def on_ready():
    print(f'{bot.user} au rapport.')

"""
@bot.command()
async def profile(ctx, username: str):
    info = get_profile(username)
    await ctx.send(f'{info}')

@bot.command()
async def score(ctx, username: str, categorie: str):
    info = get_score(username, categorie)
    await ctx.send(f'{info}')

async def send_long_message(ctx, content: str):
    chunks = [content[i:i+1900] for i in range(0, len(content), 1900)]
    for chunk in chunks:
        await ctx.send(f"```{chunk}```")
"""

async def cogs():
    await bot.load_extension("cogs.profile")
    await bot.load_extension("cogs.score")

async def main():
    await cogs()
    await bot.start(TOKEN)

asyncio.run(main())
