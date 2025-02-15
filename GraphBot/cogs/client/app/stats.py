import statistics
import discord
import json
from discord import app_commands
from discord.ext import commands
from cogs.client.app.data import data

class Stats(commands.Cog):
  def __init__(self, bot) -> None:
    self.bot = bot
    super().__init__()

  @app_commands.command(name="statistics", description="Compute stats functions")
  @app_commands.guilds(*data.appcmds)
  async def statistics(self, interaction: discord.Interaction):
    await interaction.response.send_message("Stats")
    pass

async def setup(bot: commands.Bot):
  await bot.add_cog(Stats(bot), guilds=data.appcmds)
