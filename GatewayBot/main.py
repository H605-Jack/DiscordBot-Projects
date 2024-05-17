import discord
import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix="in?", intents=intent)

@bot.event
async def on_ready():
  print("Bot is ready.")



bot.run(os.getenv("TOKEN"))