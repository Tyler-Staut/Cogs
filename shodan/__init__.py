from redbot.core.bot import Red

from .shodan import shodan


async def setup(bot: Red) -> None:
    cog = shodan(bot)
    bot.add_cog(cog)
    await cog.initialize()
