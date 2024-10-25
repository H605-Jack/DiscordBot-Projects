import json
import discord

with open("cogs/slash.json") as f:
  data = json.load(f)


appcmd_ids = []
for i in range(len(data)):
  appcmd_ids.append(discord.Object(id=data[i]["guild"]["id"]))
  

