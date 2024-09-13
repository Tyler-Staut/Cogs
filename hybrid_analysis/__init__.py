from redbot.core.bot import Red

from .hybrid_analysis import hybrid_analysis


async def setup(bot: Red) -> None:
    cog = hybrid_analysis(bot)
    bot.add_cog(cog)
    await cog.initialize()
