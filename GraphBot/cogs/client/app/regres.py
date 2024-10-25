import discord
from discord import app_commands
from discord.ext import commands
from cogs.client.app.srcs.regressions import RegressionLine
from cogs.client.app.data import data

class RegLine(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    super().__init__()
    self.bot = bot
    self.plotx = ()
    self.ploty = ()

  @app_commands.command(
    name="regression",
    description="Outputs a regression data and represent data on a graph"
  )
  @app_commands.guilds(*data.appcmd_ids)
  async def regress(self, interaction: discord.Interaction):
    await interaction.response.send_message(f"Regression of")

  @app_commands.command(
    name="regression_plots",
    description="Adding the list of plots into regression",
  )
  @app_commands.guilds(*data.appcmd_ids)
  async def regress_plots(self, interaction: discord.Interaction, plotx: int, ploty: int):
    await interaction.response.send_message(f"Added regression plot, (x: {plotx}, y: {ploty})", ephemeral=True, delete_after=1)
    
async def setup(bot: commands.Bot):
  await bot.add_cog(RegLine(bot), guilds=data.appcmd_ids)
  