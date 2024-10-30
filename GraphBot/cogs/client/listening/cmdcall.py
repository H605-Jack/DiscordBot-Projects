import discord
from discord.ext import commands
import console

class CommandCall(commands.Cog):
  def __init__(self, bot: commands.bot) -> None:
    super().__init__()
    self.bot = bot

  @commands.Cog.listener(name='on_message')
  async def cmdcall_listen(self, message: discord.Message):
    pass

  @commands.Cog.listener(name='on_message')
  async def regression_listen(self, message: discord.Message):
    from cogs.client.app.regres import RegLine as r

    # condition check on each regression line slash command
    if message.interaction.name == "regression_plots":
      console.client(f"responded to {message.author}: regression_plots content with {message.embeds}; id: {r.retrieve_regadd_id()}")
      exception_msg = "The previous message has been deleted due to timeout limit, or any users/clients with deletion privilege"
      # clean up duplicating message
      if r.retrieve_regadd_id() == 0:
        return
      else:
        try:
          rp_delmsg = await message.channel.fetch_message(r.retrieve_regadd_id())
        except Exception as e:
          console.info(f"{e}; {exception_msg}")
        finally:
          await rp_delmsg.delete()
          console.client("regression_plots: The previous message has been deleted.")
      return
    
    if message.interaction.name == "regression":
      console.client(f"responded to {message.author}: regression content with {message.embeds}; id: {r.retrieve_regress_id()}")
      # clean up duplicating error message
      if r.retrieve_regress_id() == 0:
        return
      else:
        try:
          r_delmsg = await message.channel.fetch_message(r.retrieve_regress_id())
        except Exception as e:
          console.info(f"{e}; {exception_msg}")
        finally:
          await r_delmsg.delete()
          console.client("regression: The previous message has been deleted.") 
      return


async def setup(bot: commands.Bot):
  await bot.add_cog(CommandCall(bot))
  