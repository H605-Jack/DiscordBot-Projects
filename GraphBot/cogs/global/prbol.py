from discord.ext import commands

class Parabol(commands.Cog):
  """***Physics***"""

  def __init__(self, bot) -> None:
    super().__init__()
    self.bot = bot

async def setup(bot: commands.Bot):
  await bot.add_cog(Parabol(bot))