from .shodan import ApiTools


async def setup(bot):
    await bot.add_cog(shodan(bot))
