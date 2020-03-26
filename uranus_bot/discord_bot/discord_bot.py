#!/usr/bin/env python3.7
""" Xiaomi Geeks discord Bot"""

from discord import ActivityType, Activity
from discord.ext import commands

from uranus_bot import DISCORD_TOKEN
from uranus_bot.discord_bot import DISCORD_LOGGER
from uranus_bot.discord_bot.modules import ALL_MODULES
from uranus_bot.providers.provider import Provider
from uranus_bot.utils.loader import load_modules

BOT = commands.Bot(command_prefix='!')
PROVIDER = Provider(BOT.loop)


@BOT.event
async def on_ready():
    """ Confirm the bot is ready """
    DISCORD_LOGGER.info("Bot started as %s! Username is %s and ID is %s",
                        BOT.user.name, BOT.user, BOT.user.id)
    activity = Activity(name='Xiaomi updates', type=ActivityType.watching)
    await BOT.change_presence(activity=activity)


# Load all modules in modules list
load_modules(ALL_MODULES, __package__)


def main():
    """Run the bot."""
    BOT.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
