from discord.ext import commands
from utils.score import get_score
from utils.long import split

class Score(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def score(self, ctx, username: str, *, category: str = None):
        output = get_score(username, category)
        for chunk in split(output):
            await ctx.send(chunk)

async def setup(bot):
    await bot.add_cog(Score(bot))
