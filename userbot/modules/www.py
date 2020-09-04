# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.dc$")
async def neardc(event):
    """ For .dc command, get the nearest datacenter information. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Country : `{result.country}`\n"
                     f"Nearest Datacenter : `{result.nearest_dc}`\n"
                     f"This Datacenter : `{result.this_dc}`")


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pong!\n%sms`" % (duration))


CMD_HELP.update(
    {"dc": ".dc\
    \nUsage: Finds the nearest datacenter from your server."})
CMD_HELP.update(
    {"ping": ".ping\
    \nUsage: Shows how long it takes to ping your bot."})
