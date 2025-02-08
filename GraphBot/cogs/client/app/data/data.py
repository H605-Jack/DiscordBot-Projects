import json
import discord
import os
from dotenv import load_dotenv
load_dotenv()

with open(os.getenv("authsrc")) as f:
  data = json.load(f)
appcmd_ids = []
for i in range(len(data)):
  appcmd_ids.append(discord.Object(id=data["discord_auth"][i]["guild"]["id"]))
  