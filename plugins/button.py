from pyrogram import *
from pyrogram.types import *

BSTART = InlineKeyboardMarkup([
            [
              InlineKeyboardButton(text="Developer👤", url="https://t.me/MSDZULQRNN"),
            ],
            [
              InlineKeyboardButton(text="Tutorial💡", callback_data="tutor"),
              InlineKeyboardButton(text="Donasi💌", callback_data="donasi"),
            ],
            [
              InlineKeyboardButton(text="Channel", url="https://t.me/MSPR0JECT"),
              InlineKeyboardButton(text="Support", url="https://t.me/envSample"),
            ],
            [
              InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ])