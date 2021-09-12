import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
OWNER_ID = os.environ.get("OWNER_ID")


@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """ᴀɴᴅᴀ ᴍᴇᴍʙᴜᴛᴜʜᴋᴀɴ ʙᴀɴᴛᴜᴀɴ ?? 🧐

★ ᴋɪʀɪᴍᴋᴀɴ sᴀᴊᴀ sᴀʏᴀ ғɪʟᴇ, sᴀʏᴀ ᴀᴋᴀɴ ᴍᴇɴʏɪᴍᴘᴀɴ ғɪʟᴇ ᴅᴀɴ ᴍᴇᴍʙᴇʀɪ ᴀɴᴅᴀ ᴛᴀᴜᴛᴀɴ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴅɪʙᴀɢɪᴋᴀɴ

ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ᴅɪ sᴀʟᴜʀᴀɴ ᴊᴜɢᴀ 😉

★  ᴊᴀᴅɪᴋᴀɴ sᴀʏᴀ ᴀᴅᴍɪɴ ᴅɪ ᴄʜᴀɴɴᴇʟ ᴀɴᴅᴀ ᴅᴇɴɢᴀɴ ɪᴢɪɴ ᴇᴅɪᴛ. ᴄᴜᴋᴜᴘ sᴇᴋᴀʀᴀɴɢ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴍᴇɴɢᴜɴɢɢᴀʜ ғɪʟᴇ ᴅɪ ᴄʜᴀɴɴᴇʟ sᴀʏᴀ ᴀᴋᴀɴ ᴍᴇɴɢᴇᴅɪᴛ sᴇᴍᴜᴀ ᴘᴏsᴛɪɴɢ ᴅᴀɴ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴜʀʟ ᴛᴀᴜᴛᴀɴ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴅɪʙᴀɢɪᴋᴀɴ.‌.‌‌"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Home 🏕', callback_data='home'),
            InlineKeyboardButton('About 📕', callback_data='about')
        ],
        [
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]
    ]

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


@Client.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    owner = await c.get_users(int(OWNER_ID))
    bot = await c.get_me()

    # about text
    about_text = f"""--**My Details:**--

🤖 𝐌𝐲 𝐍𝐚𝐦𝐞: {bot.mention(style='md')}
    
📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: [Python 3](https://www.python.org/)

🧰 𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤: [Pyrogram](https://github.com/pyrogram/pyrogram)

👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫:

📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: [Duniamovie](https://t.me/joinchat/GZ0yLAPeD25lYWQ1)

👥 𝐆𝐫𝐨𝐮𝐩: [𝕊𝕦𝕡𝕡𝕠𝕣𝕥 𝔾𝕣𝕦𝕡 ❤️](https://t.me/joinchat/HwxSD2aHHHU0OWU1)

🌐𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞: [Press Me 🥰](https://github.com/Ns-Bots/TG-File-Store)
"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Home 🏕', callback_data='home'),
            InlineKeyboardButton('Help 💡', callback_data='help')
        ],
        [
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]
    ]

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)
