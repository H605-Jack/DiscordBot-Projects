import discord
from discord import app_commands
from discord.ext import commands
from cogs.client.app.srcs.regressions import RegressionLine
from cogs.client.app.data import data

class RegLine(commands.Cog):
  __regress_id = 0
  __regress_add_id = 0
  def __init__(self, bot: commands.Bot) -> None:
    super().__init__()
    self.bot = bot
    self.plotx = []
    self.ploty = []

  # retrieve slash command ids
  @classmethod
  def retrieve_regress_id(cls):
    return cls.__regress_id
  
  @classmethod
  def retrieve_regadd_id(cls):
    return cls.__regress_add_id

  @app_commands.command(
    name="regression",
    description="Outputs a regression data and represent data on a graph"
  )
  @app_commands.guilds(*data.appcmd_ids)
  async def regress(self, interaction: discord.Interaction):
    # embed template
    embed = discord.Embed(
        title="Regression Data",
        description=f"x: {self.plotx},\n y: {self.ploty}"
      )
    #embed.add_field(value="Choose one to show...")

    # Requirement: Ensure that there are at least 2 x and y values
    if len(self.plotx) >= 2 and len(self.ploty) >= 2:
      await interaction.response.send_message(embed=embed)
    else:
      await interaction.response.send_message(embed=discord.Embed(
        description=":no_entry: - At least two x and y values required", color=discord.Color.from_rgb(255, 0, 0)
      ))
      origin = await interaction.original_response()
      RegLine.__regress_id = origin.id

  @app_commands.command(
    name="regression_plots",
    description="Adding the list of plots into regression",
  )
  @app_commands.guilds(*data.appcmd_ids)
  async def regress_plots(self, interaction: discord.Interaction, plotx: int, ploty: int):
    """
    Adding plots for regressions
    """
    self.plotx.append(plotx)
    self.ploty.append(ploty)
    # send an embed message privately to the user
    await interaction.response.send_message(embed=discord.Embed(description=f"Added regression plot, (x: {plotx}, y: {ploty})"), delete_after=45)
    origin = await interaction.original_response()
    RegLine.__regress_add_id = origin.id
    
async def setup(bot: commands.Bot):
  await bot.add_cog(RegLine(bot), guilds=data.appcmd_ids)
  