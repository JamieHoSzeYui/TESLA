# For The-TG-Bot v3
# By Priyam Kalra

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoto
from userbot.events import register
from userbot import CMD_HELP

import STORAGE

STORAGE.userObj = False


@register(outgoing=True, pattern=r"\.clone ?(.*)")
async def clone(event):
    if event.fwd_from:
        return
    inputArgs = event.pattern_match.group(1)
    if "-r" in inputArgs:
        await event.edit("`Reverting to my true identity..`")
        if not STORAGE.userObj:
            return await event.edit("`You need to clone a profile before reverting!`")
        await updateProfile(STORAGE.userObj, reset=True)
        await event.edit("`Feels good to be back.`")
        return
    elif "-d" in inputArgs:
        STORAGE.userObj = False
        await event.edit("`The profile backup has been nuked.`")
        return
    if not STORAGE.userObj:
        STORAGE.userObj = await event.client(GetFullUserRequest(event.from_id))
    logger.info(STORAGE.userObj)
    STORAGE.userObj = await getUserObj(event)
    await event.edit("`Stealing this random person's identity..`")
    await updateProfile(STORAGE.userObj)
    await event.edit("`I am you and you are me.`")


async def updateProfile(STORAGE.userObj, reset=False):
    firstName = "Deleted Account" if STORAGE.userObj.user.first_name is None else STORAGE.userObj.user.first_name
    lastName = "" if STORAGE.userObj.user.last_name is None else STORAGE.userObj.user.last_name
    userAbout = STORAGE.userObj.about if STORAGE.userObj.about is not None else ""
    userAbout = "" if len(userAbout) > 70 else userAbout
    if reset:
        userPfps = await client.get_profile_photos('me')
        userPfp = userPfps[0]
        await client(DeletePhotosRequest(
            id=[InputPhoto(
                id=userPfp.id,
                access_hash=userPfp.access_hash,
                file_reference=userPfp.file_reference
            )]))
    else:
        try:
            userPfp = STORAGE.userObj.profile_photo
            pfpImage = await client.download_media(userPfp)
            await client(UploadProfilePhotoRequest(await client.upload_file(pfpImage)))
        except BaseException:
            pass
    await client(UpdateProfileRequest(
        about=userAbout, first_name=firstName, last_name=lastName
    ))


async def getUserObj(event):
    if event.reply_to_msg_id:
        replyMessage = await event.get_reply_message()
        if replyMessage.forward:
            STORAGE.userObj = await event.client(
                GetFullUserRequest(replyMessage.forward.from_id or replyMessage.forward.channel_id
                                   )
            )
            return STORAGE.userObj
        else:
            STORAGE.userObj = await event.client(
                GetFullUserRequest(replyMessage.from_id)
            )
            return STORAGE.userObj


CMD_HELP.update({"clone": "\
`.clone` (as a reply to a message of a user)\
\nUsage: Steals the user's identity.\
\n\n`.clone -r/-reset`\
\nUsage: Revert back to your true identity.\
\n\n`.clone -d/-del`\
\nUsage: Delete your profile's backup on your own risk.\
"})
