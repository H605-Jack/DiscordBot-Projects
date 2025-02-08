import discord
import os
import platform
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
with open("cogs/slash.json") as f:
  data = json.load(f)

# identifying system
status.log(f"API runtime location\nsystem: {platform.system()}\narch: {platform.processor()}\nnode: {platform.node()}")

async def load_dir(dir: str) -> None:
  for filename in os.listdir(f"cogs/client/{dir}"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.client.{dir}.{filename[:-3]}")

### bot status
@bot.event
async def on_connect():
  status.client("Client is online. Syncing features...")

@bot.event
async def on_ready():
  for i in range(len(data)):
    syncs = await bot.tree.sync(guild=discord.Object(id=data[i]["guild"]["id"]))
  status.client("Bot is ready.")
  status.log(f"Synced {len(syncs)} app command(s).")

@bot.event
async def on_disconnect():
  status.client("Client bot is disconnected.")

### cogs reloading
@bot.command(name="update")
@commands.has_permissions(administrator=True)
async def cog_reload(ctx: commands.Context, dir: str):
  # delete the author's message
  msg = await ctx.fetch_message(ctx.message.id)
  await msg.delete()
  await ctx.send("**INFO:** Cogs are currently updating. Check the log messages for informations.", ephemeral=True, delete_after=3)
  print(status.log("Cog reload requested..."))
  tsa = status.timestamp() 
 
  # Reloading the cogs
  try:
    for filename in os.listdir(f"cogs/client/{dir}"):
      if filename.endswith(".py"):
        await bot.reload_extension(f"cogs.client.{dir}.{filename[:-3]}")
        tsb = status.timestamp()
  except Exception as e:
    print(status.error(f"Failed to reload the cogs: {e}"))
    return
  print(status.log(f"Cog reload finished in {round(tsb - tsa, 2)}s."))

### initiate runtime
async def main():
  await load_dir("app")
  await load_dir("global")
  await load_dir("listening")
  await bot.start(os.getenv("TOKEN"))
  
loop = asyncio.new_event_loop()
try:
  loop.run_until_complete(main())
except KeyboardInterrupt as e:
  print() # output line break
  # disconnecting the bot from client and cleaning up app commands
  if not bot.is_closed():
    loop.run_until_complete(bot.close())
    status.client("Client has successfully disconnected")
finally:
  # stop the loop
  if not loop.is_closed():
    loop.close()
    status.log("Session completed.")
