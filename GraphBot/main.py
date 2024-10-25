import discord
import os
import asyncio
import json
import console as status
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix="g!", intents=intent)

async def load_dir(dir: str) -> None:
  for filename in os.listdir(f"cogs/client/{dir}"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.client.{dir}.{filename[:-3]}")

# cogs reloading
@bot.command(name="update")
@commands.has_permissions(administrator=True)
async def cog_reload(ctx: commands.Context, dir: str):
  await ctx.send("**INFO:** Cogs are currently updating. Check the log messages for informations.", ephemeral=True, delete_after=3)
  print(status.log("Cog reload requested..."))
  try:
    for filename in os.listdir(f"cogs/client/{dir}"):
      if filename.endswith(".py"):
        await bot.reload_extension(f"cogs.client.{dir}.{filename[:-3]}")
  except Exception as e:
    print(status.error(f"Failed to reload the cogs: {e}"))
  print(status.log("Cog reload finished."))

with open("cogs/slash.json") as f:
  data = json.load(f)
  
# bot status
@bot.event
async def on_connect():
  print(status.client("Client is online. Updating features..."))

@bot.event
async def on_ready():
  for i in range(len(data)):
    syncs = await bot.tree.sync(guild=discord.Object(id=data[i]["guild"]["id"]))
  print(status.client("Bot is ready."))
  print(status.log(f"Synced {len(syncs)} app command(s)."))

# initiate runtime
async def main():
  await load_dir("app")
  await load_dir("global"),
  await bot.start(os.getenv("TOKEN"))
  
loop = asyncio.new_event_loop()
try:
  loop.run_until_complete(main())
except KeyboardInterrupt as e:
  print() # output line break
  # disconnecting the bot from client and cleaning up app commands
  if not bot.is_closed():
    loop.run_until_complete(bot.close())
    print(status.client("Client has successfully disconnected"))
finally:
  # stop the loop
  if not loop.is_closed():
    loop.close()
    print(status.log("Session completed."))
