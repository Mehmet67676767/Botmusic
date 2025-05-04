
# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import os
from datetime import datetime
from pathlib import Path

from pyrogram.enums import ParseMode
from config import LOG_GROUP_ID
from AlexaMusic.utils.database import is_on_off
from AlexaMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝖯𝗅𝖺𝗒 𝖫𝗈𝗀</b>

<b>𝖢𝗁𝖺𝗍 𝖨𝖣 :</b> <code>{message.chat.id}</code>
<b>𝖢𝗁𝖺𝗍 𝖭𝖺𝗆𝖾 :</b> {message.chat.title}
<b>𝖢𝗁𝖺𝗍 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :</b> @{message.chat.username}

<b>𝖴𝗌𝖾𝗋 𝖨𝖣 :</b> <code>{message.from_user.id}</code>
<b>𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾 :</b> {message.from_user.mention}
<b>𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :</b> @{message.from_user.username}

<b>𝖰𝗎𝖾𝗋𝗒 :</b> {message.text.split(None, 1)[1]}
<b>𝖲𝗍𝗋𝖾𝖺𝗆-𝖳𝗒𝗉𝖾 :</b> {streamtype}"""

        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass

        try:
            log_dir = Path("logs")
            log_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file = log_dir / f"{datetime.now().strftime('%Y-%m-%d')}.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message.from_user.first_name} (ID: {message.from_user.id}) "
                        f"played '{message.text.split(None, 1)[1]}' in group '{message.chat.title}' "
                        f"(ID: {message.chat.id}) | Type: {streamtype}\n")
        except Exception as e:
            print(f"[TXT LOG HATASI] {e}")
