""" TWRP messages generator """
from discord import Embed

from uranus_bot.providers.custom_recovery.twrp.twrp import get_twrp


async def twrp_message(device, twrp_data):
    """ Generate discord message of twrp command """
    data = await get_twrp(device, twrp_data)
    embed = Embed(title=f'**Latest TWRP for {data["name"]}:**',
                  description=f'**Updated:** {data["date"]}\n')
    embed.add_field(name=f'{data["dl_file"]} - {data["size"]}',
                    value=f'[Download]({data["dl_link"]})')
    return embed
