import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix="g!", intents=intent)

async def load_dir(dir: str) -> None:
  for filename in os.listdir(f"cogs/{dir}"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.{dir}.{filename[:-3]}")

# bot status
@bot.event
async def on_ready():
  print("Bot is ready.")

# initiate runtime
async def main():
  await load_dir("global"),
  await load_dir("listening"),
  await bot.start(os.getenv("TOKEN"))
  
# runtime
loop = asyncio.new_event_loop()
try:
  loop.run_until_complete(main())
except KeyboardInterrupt as e:
  # Termination requested
  print("\nTermination Requested. Bot is shutting down...")
  if not loop.is_closed():
    loop.close()
    print("Bot has successfully disconnected.")
