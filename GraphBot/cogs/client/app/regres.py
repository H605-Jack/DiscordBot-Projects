import discord
import json
from discord import app_commands
from discord.ext import commands
from cogs.client.app.srcs.regressions import RegressionLine
from cogs.client.app.data import data

ids = data.retrieve_sids()

class RegLine(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    super().__init__()
    self.bot = bot
    
async def setup(bot: commands.Bot):
  await bot.add_cog(RegLine(bot), guilds=ids)
  