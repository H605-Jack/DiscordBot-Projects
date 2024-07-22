import discord
import json
from discord.ext import commands
from cogs.client.app.general import parabol
from discord import app_commands

appcmd_ids = []

with open("../../www/port/80/api/auth/discord/track/authoutput.json") as f:
  data = json.load(f)

for i in range(len(data)):
  appcmd_ids.append(discord.Object(id=data[i]["guild"]["id"]))

class Parabola(commands.Cog):
  """
  Physics
  -----------------
  
  Calculate the projectile motion
  """
  def __init__(self, bot: commands.Bot) -> None:
    super().__init__()
    self.bot = bot

  @app_commands.command(name="parabola", description="abc")
  @app_commands.guilds(*appcmd_ids)
  async def parabola(self, interaction: discord.Interaction):
    await interaction.response.send_message("abc");

async def setup(bot: commands.Bot):
  await bot.add_cog(Parabola(bot), guilds=appcmd_ids)
