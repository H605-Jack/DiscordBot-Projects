import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intent = discord.Intents.default()
perm = discord.Permissions()
intent.members = True
intent.message_content = True
perm.read_message_history = True
bot = commands.Bot(command_prefix="in?", intents=intent)

async def load_file(dir: str) -> None:
  for filename in os.listdir(f"cogs/{dir}"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.{dir}.{filename[:-3]}")

# bot status
@bot.event
async def on_ready():
  print("Bot is ready.")

# runtime
async def main():
  await asyncio.gather(
    load_file("global"),
    load_file("listening"),
    bot.start(os.getenv("TOKEN"))
  )

loop = asyncio.new_event_loop()
try:
  loop.run_until_complete(main())
except KeyboardInterrupt as e:
  loop.run_until_complete(bot.close())
  print("Exception")
finally:
  loop.close()