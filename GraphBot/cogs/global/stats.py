from discord.ext import commands

class Stats(commands.Cog):
  def __init__(self, bot) -> None:
    self.bot = bot
    super().__init__()

  @commands.command(name="stats")
  async def statistics(self, ctx: commands.Context):
    print("stats command registered")
    pass

async def setup(bot: commands.Bot):
  await bot.add_cog(Stats(bot))

