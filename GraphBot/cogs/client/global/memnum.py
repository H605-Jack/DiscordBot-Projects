from discord.ext import commands

class MemoryNumber(commands.Cog):
  def __init__(self, bot) -> None:
    super().__init__()
    self.bot = bot
    self.numbers = 0

  @commands.command(name="sto")
  async def sto(self, ctx: commands.Context, *numbers: float):
    self.numbers = len(numbers)
    await ctx.send(f"Stored {self.numbers} numbers.")
    pass

  @commands.command(name="rcl")
  async def rcl(self, ctx: commands.Context):
    await ctx.send(f"Recalling {self.numbers} numbers")
    pass

async def setup(bot: commands.Bot):
  await bot.add_cog(MemoryNumber(bot))