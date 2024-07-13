import discord
import os
import asyncio
import time
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

def status_log(message: str):
  print(f"[{time.strftime("%H:%M:%S")}] {message}")

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
async def on_connect():
  status_log("Client is online. Updating features...")

@bot.event
async def on_ready():
  status_log("Bot is ready.")

# initiate runtime
async def main():
  #await load_dir("app")
  await load_dir("global"),
  await bot.start(os.getenv("TOKEN"))
  
# runtime
loop = asyncio.new_event_loop()
try:
  loop.run_until_complete(main())
except KeyboardInterrupt as e:
  # Termination requested
  print() # output line break
  loop.run_until_complete(bot.close())
  if bot.is_closed():
    status_log("Client has successfully disconnected")
finally:
  loop.close()
  if loop.is_closed():
    status_log("Session completed.")

