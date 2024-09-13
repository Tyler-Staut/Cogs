from .hybrid_analysis import ApiTools


async def setup(bot):
    await bot.add_cog(hybrid_analysis(bot))
