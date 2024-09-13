from typing import Literal

import discord
import sys
import pkgutil
import os
import importlib

from . import modules

from .modules import search

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config


from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.chat_formatting import escape, pagify
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class shodan_cog(commands.Cog):
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
        api_token = await self.bot.get_shared_api_tokens("shodan")
        self.api_token = api_token

        for importer, module_name, is_pkg in pkgutil.iter_modules(modules.__path__):
            if module_name not in self.modules:
                self.modules.append(module_name)

    async def red_delete_data_for_user(self, *, requester: RequestType, user_id: int) -> None:
        # TODO: Replace this with the proper end user data removal handling.
        super().red_delete_data_for_user(requester=requester, user_id=user_id)

    @commands.group()
    async def shodan(self, ctx):
        api_token = self.api_token
        if api_token.get("api_key") is None:
            return await ctx.send("The Shodan API key has not been set.")
        # Use the API key to access content as you normally would

    @shodan.command()
    async def modules(self, ctx):
        """
        List all available modules
        """
        modules_list = ""
        for module in self.modules:
            modules_list += f"{module}\n"

        await ctx.send("Current Supported Functions:")
        await ctx.send(modules_list)


    @shodan.command()
    async def upload(self, ctx, *, query: str):
        """This does stuff!"""
        # Your code will go here
        embed = upload.get_result(query, self.api_token)
        await ctx.send(embed=embed)
