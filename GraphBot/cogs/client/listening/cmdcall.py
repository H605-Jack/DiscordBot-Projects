import discord
from discord.ext import commands
from cogs.client.app.regres import RegLine as r

class CommandCall(commands.Cog):
  def __init__(self, bot: commands.bot) -> None:
    super().__init__()
    self.bot = bot

  @commands.Cog.listener(name='on_message')
  async def cmdcall_listen(self, message: discord.Message):
    pass

  @commands.Cog.listener(name='on_message')
  async def regression_listen(self, message: discord.Message):
    if message.interaction.name == "regression":
      print(f"responded to {message.author}: {message.embeds}")
      print(r.retrieve_foreign_value())
      # delete if duplicated error message
      
      delmsg = await message.channel.fetch_message(r.retrieve_foreign_value())
      print(type(delmsg))

async def setup(bot: commands.Bot):
  await bot.add_cog(CommandCall(bot))
  