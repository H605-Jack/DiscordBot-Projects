import discord
from discord.ext import commands
from discord import app_commands

class MemoryNumber(commands.Cog):
  def __init__(self, bot) -> None:
    super().__init__()
    self.bot = bot

  @app_commands.command(name="store", description="Store a number")
  async def sto(self, interaction: discord.Interaction):
    pass

  @app_commands.command(name="recall", description="Recall a number")
  async def rcl(self, interaction: discord.Interaction):
    pass
