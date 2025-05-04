#Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >

#Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""" TheTeamAlexa is a project of Telegram bots with variety of purposes. Copyright (c) 2021 ~ Present Team Alexa https://github.com/TheTeamAlexa

This program is free software: you can redistribute it and can modify as you want or you can collabe if you have new ideas. """

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_GROUP, SUPPORT_CHANNEL
import random

def generate_dynamic_bar(played, dur, length=13): try: played_sec = int(played.split(":")[0]) * 60 + int(played.split(":")[1]) dur_sec = int(dur.split(":")[0]) * 60 + int(dur.split(":")[1]) filled_len = int(length * played_sec / dur_sec) bar = "▰" * filled_len + "▱" * (length - filled_len) return bar except: return "▰" * length

def stream_markup_timer(_, videoid, chat_id, played, dur): bar = generate_dynamic_bar(played, dur) buttons = [ [InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer")], [ InlineKeyboardButton("⏮", callback_data=f"ADMIN Previous|{chat_id}"), InlineKeyboardButton("⏸", callback_data=f"ADMIN Pause|{chat_id}"), InlineKeyboardButton("▶️", callback_data=f"ADMIN Resume|{chat_id}"), InlineKeyboardButton("⏭", callback_data=f"ADMIN Skip|{chat_id}") ], [ InlineKeyboardButton("⭐ Listeye Ekle", callback_data=f"add_playlist {videoid}"), InlineKeyboardButton("🎧 Şarkı Bilgisi", callback_data=f"info {videoid}") ], [ InlineKeyboardButton("👍 0", callback_data=f"like {videoid}"), InlineKeyboardButton("👎 0", callback_data=f"dislike {videoid}") ], [ InlineKeyboardButton("📃 Kuyruk", callback_data=f"queue {chat_id}"), InlineKeyboardButton("⭐ Favorilerim", callback_data="my_favs") ], [ InlineKeyboardButton("🎉 Parti Mod", callback_data=f"mode party"), InlineKeyboardButton("☁️ Chill Mod", callback_data=f"mode chill") ], [ InlineKeyboardButton("➕ Şarkı İste", switch_inline_query_current_chat="Şarkı adı...") ], [ InlineKeyboardButton("⚙ Ayarlar", callback_data=f"PanelMarkup {videoid}|{chat_id}"), InlineKeyboardButton("❌ Kapat", callback_data="close") ] ] return buttons

def stream_markup(_, videoid, chat_id): return [[InlineKeyboardButton("▶️ Oynat", callback_data=f"add_playlist {videoid}")]]

def telegram_markup(_, chat_id): return [[ InlineKeyboardButton("⚙️ Ayarlar", callback_data=f"PanelMarkup None|{chat_id}"), InlineKeyboardButton("❌ Kapat", callback_data="close") ]]

def close_keyboard(): return InlineKeyboardMarkup([[InlineKeyboardButton(text="❌ Kapat", callback_data="close"),
        ],
    ]
    return buttons



def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


## By Anon
close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝖢𝗅𝗈𝗌𝖾", callback_data="close")]]
)

## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⇆ sʜᴜғғʟᴇ ⇆",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="↻ ʟᴏᴏᴩ ↻", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ 10 sᴇᴄᴏɴᴅ",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 10 sᴇᴄᴏɴᴅ",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ 30 sᴇᴄᴏɴᴅ",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 30 sᴇᴄᴏɴᴅ",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="↻ ʙᴀᴄᴋ ↻",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


## Queue Markup Anon


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="☆", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="𝖢𝗅𝗈𝗌𝖾", callback_data=f"ADMIN CloseA|{chat_id}")],
    ]
    return buttons
