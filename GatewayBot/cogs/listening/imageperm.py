import discord
from discord.ext import commands

class ImagePermission(commands.Cog):
  def __init__(self, bot) -> None:
    super().__init__()
    self.bot = bot
    self.embed = discord.Embed()

  # check for images and attachments posted in the server
  @commands.Cog.listener()
  async def on_message(self, message: discord.Message):
    if message.attachments:
      # check for list of channels (prioritizing filtered channels with no effects )

      # set the timer before delete the attachment
      await message.reply("30-Minute Image Permission Applied")
      

async def setup(bot: commands.Bot):
  await bot.add_cog(ImagePermission(bot))