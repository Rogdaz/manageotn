import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/d0619994d9ed62070ef76.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm DazRepo Robot.** \n\n"
  TEXT += "β΅ **I'm Working Properly** \n"
  TEXT += f"β΅ **My Master : [β πΏπΌπππ β](tg://openmessage?user_id=2056203142)** \n"
  TEXT += f"β΅ **Library Version :** `{telever}` \n"
  TEXT += f"β΅ **Telethon Version :** `{tlhver}` \n"
  TEXT += f"β΅ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here βοΈ**"
  BUTTON = [[Button.url("Help", "tg://openmessage?user_id=2056203142"), Button.url("Support", "https://t.me/about_db")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
