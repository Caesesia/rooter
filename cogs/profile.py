from discord.ext import commands
from utils.profile import get_profile  # or wherever you store it
from utils.long import split

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, username: str):
        try:
            output = get_profile(username)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            return

        for chunk in split(output):
            await ctx.send(chunk)

async def setup(bot):
    await bot.add_cog(Profile(bot))
