import discord
import os
from dotenv import load_dotenv
load_dotenv()

appcmds = [];
for _id in os.listdir(os.getenv("authsrc")):
  data = _id[14:-5]
  if data != "":
    appcmds.append(discord.Object(id=int(data)))
