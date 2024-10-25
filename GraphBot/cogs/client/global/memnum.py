from discord.ext import commands

class MemoryNumber(commands.Cog):
  def __init__(self, bot) -> None:
    super().__init__()
    self.bot = bot
    self.numbers = ()
    # plots storage
    self.plotx = ()
    self.ploty = ()

  @commands.command(name="sto")
  async def sto(self, ctx: commands.Context, *numbers: int | float):
    self.numbers = self.numbers + numbers
    await ctx.send(f"Stored {len(self.numbers)} numbers.")
    print(f"{type(self.numbers)} {self.numbers}")
    pass

  @commands.command(name="rcl")
  async def rcl(self, ctx: commands.Context, rcloption: str):
    """
    Recalling the list of numbers that has been stored

    params: 
      `rcloption: str` - what to recall 
    """
    await ctx.send(f"Recalling {len(self.numbers)} numbers: {self.numbers}")
    pass

async def setup(bot: commands.Bot):
  await bot.add_cog(MemoryNumber(bot))