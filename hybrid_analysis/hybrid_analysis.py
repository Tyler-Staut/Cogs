from typing import Literal

import discord
import sys
import pkgutil
import os
import importlib
import aiohttp

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.chat_formatting import escape, pagify
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu


RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class hybrid_analysis(commands.Cog):
    """
    Hybrid Analysis for Discord
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=1,
            force_registration=True,
        )
        self.api_token = None
        self.modules = []

    async def initialize(self):
        api_token = await self.bot.get_shared_api_tokens("hybrid-analysis")
        self.api_token = api_token

    @commands.group()
    async def hybrid_analysis(self, ctx):
        api_token = self.api_token
        if api_token.get("api_key") is None:
            return await ctx.send("The Hybrid Analysis API key has not been set.")
        # Use the API key to access content as you normally would

    @hybrid_analysis.command()
    async def modules(self, ctx):
        """
        List all available modules
        """
        modules_list = ""
        for module in self.modules:
            modules_list += f"{module}\n"

        await ctx.send("Current Supported Functions:")
        await ctx.send(modules_list)

    @hybrid_analysis.command()
    async def upload(self, ctx, *, query: str = None):
        """Upload a file or URL to Hybrid Analysis for scanning"""
        if ctx.message.attachments:
            # Handle file upload
            file = ctx.message.attachments[0]
            file_bytes = await file.read()
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://www.hybrid-analysis.com/api/v2/quick-scan/file",
                    headers={"api-key": self.api_token["api_key"]},
                    data={"file": file_bytes},
                ) as response:
                    result = await response.json()
                    await ctx.send(f"Scan result: {result}")
