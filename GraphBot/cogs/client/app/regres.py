import discord
from discord import app_commands
from discord.ext import commands
from cogs.client.app.srcs.regressions import RegressionLine
from cogs.client.app.data import data

class RegLine(commands.Cog):
  __foreign_value = 0
  def __init__(self, bot: commands.Bot) -> None:
    super().__init__()
    self.bot = bot
    self.plotx = []
    self.ploty = []

  @classmethod
  def retrieve_foreign_value(cls):
    return cls.__foreign_value

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
      try:
        origin = await interaction.original_response()
        RegLine.__foreign_value = origin.id
      except Exception as e:
        print(e)

  @app_commands.command(
    name="regression_plots",
    description="Adding the list of plots into regression",
  )
  @app_commands.guilds(*data.appcmd_ids)
  async def regress_plots(self, interaction: discord.Interaction, _plotx: int, _ploty: int):
    """
    Adding plots for regressions
    """
    self.plotx.append(_plotx)
    self.ploty.append(_ploty)
    # send an embed message privately to the user
    await interaction.response.send_message(embed=discord.Embed(description=f"Added regression plot, (x: {_plotx}, y: {_ploty})"), ephemeral=True, delete_after=5)
    
async def setup(bot: commands.Bot):
  await bot.add_cog(RegLine(bot), guilds=data.appcmd_ids)
  