import discord
from discord import app_commands
from discord.ext import commands
from cogs.client.app.data import data

class Derivative(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    super().__init__()
    
  @app_commands.command(name="derivative")
  @app_commands.guilds(*data.appcmds)
  async def derivative(self, interaction: discord.Interaction):
    await interaction.response.send_message("Usage: /derivative <function>")
    pass
  pass

async def setup(bot: commands.Bot):
  await bot.add_cog(Derivative(bot), guilds=data.appcmds)