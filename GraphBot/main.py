import discord
import os
import asyncio
import time
import json
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
  for filename in os.listdir(f"cogs/client/{dir}"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.client.{dir}.{filename[:-3]}")

with open("../../www/port/80/api/auth/discord/track/authoutput.json") as f:
  data = json.load(f)
  
# bot status
@bot.event
async def on_connect():
  status_log("Client is online. Updating features...")

@bot.event
async def on_ready():
  for i in range(len(data)):
    apps = await bot.tree.sync(guild=discord.Object(id=data[i]["guild"]["id"]))
  status_log("Bot is ready.")
  print(apps)

# register app commands
@bot.command(name="register")
async def register(ctx: commands.Context):
  await ctx.send("registered")

# initiate runtime
async def main():
  await load_dir("app")
  await load_dir("global"),
  await bot.start(os.getenv("TOKEN"))
  
# runtime
loop = asyncio.new_event_loop()
try:
  loop.run_until_complete(main())
except KeyboardInterrupt as e:
  print() # output line break
  # disconnecting the bot from client and cleaning up app commands
  if not bot.is_closed():
    loop.run_until_complete(bot.close())
    status_log("Client has successfully disconnected")
finally:
  # stop the loop
  if not loop.is_closed():
    loop.close()
    status_log("Session completed.")

