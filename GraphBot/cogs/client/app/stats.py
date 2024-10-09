import statistics
import discord
import json
from srcs.regressions import RegressionLine
from discord import app_commands
from discord.ext import commands

appcmd_ids = []

with open("cogs/slash.json") as f:
  data = json.load(f)

for i in range(len(data)):
  appcmd_ids.append(discord.Object(id=data[i]["guild"]["id"]))

class Stats(commands.Cog):
  def __init__(self, bot) -> None:
    self.bot = bot
    super().__init__()

  @app_commands.command(name="statistics", description="Compute stats functions")
  @app_commands.guilds(*appcmd_ids)
  async def statistics(self, interaction: discord.Interaction):
    await interaction.response.send_message("Stats")
    pass

async def setup(bot: commands.Bot):
  await bot.add_cog(Stats(bot), guilds=appcmd_ids)
