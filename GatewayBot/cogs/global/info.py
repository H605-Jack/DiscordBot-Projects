from discord.ext import commands

class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  """
  Sending the status of the server
  """
  @commands.command(name="info")
  async def info(self, ctx: commands.Context):
    await ctx.send("info")
    pass
  pass

async def setup(bot: commands.Bot):
  await bot.add_cog(Info(bot))