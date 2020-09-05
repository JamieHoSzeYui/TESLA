# For The-TG-Bot v3
# Created By @loxxi
# Modified by @TechyNewbie (23/08/20)
# Modified by @justaprudev (28/08/20)
# Ported to TESLA by @JamieHoSzeYui

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"\.htg ?(.*)")
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    query = input_str.replace(" ", "+")
    url = f"https://lmgtfy.com/?q={query}&iie=1"
    try:
        webpage = requests.get(url).text
        if webpage:
            await event.edit(f"More info about \"[{input_str}]({url})\"")
    except BaseException:
        await event.edit(f"More info about \"[{input_str}]({url})\"")


CMD_HELP.update({"htg": "\
`.htg <query>`\
\nUsage: A guide on how to search on google.\
"})

