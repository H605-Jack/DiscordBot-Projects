from discord.ext import commands

class MemoryNumber(commands.Cog):
  def __init__(self, bot) -> None:
    super().__init__()
    self.bot = bot
    self.numbers = ()

  @commands.command(name="sto")
  async def sto(self, ctx: commands.Context, *numbers: int | float):
    self.numbers = self.numbers + numbers
    await ctx.send(f"Stored {len(self.numbers)} numbers.")
    print(self.numbers)
    pass

  @commands.command(name="rcl")
  async def rcl(self, ctx: commands.Context):
    await ctx.send(f"Recalling {len(self.numbers)} numbers: {self.numbers}")
    pass

async def setup(bot: commands.Bot):
  await bot.add_cog(MemoryNumber(bot))