#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>𝖳𝗁𝗂𝗌 𝖨𝗌 𝖠 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖥𝗂𝗅𝖾 𝖲𝖺𝗏𝖾𝗋 𝖡𝗈𝗍. \n\n➜ 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄. \n➜ 𝖶𝗈𝗋𝗄𝗌 𝖨𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈𝗈. \n➜ 𝖠𝗏𝗈𝗂𝖽 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖨𝗇𝖿𝗋𝗂𝗇𝗀𝖾𝗆𝖾𝗇𝗍. \n\n★ 𝗔𝗯𝗼𝘂𝘁 𝗙𝗶𝗹𝗲 𝗦𝗮𝘃𝗲𝗿 \n\n๏ 𝖡𝗈𝗍 𝖭𝖺𝗆𝖾 ➜ <a href='https://t.me/TeamLegendSaver_Bot'>ʟᴇɢᴇɴᴅ ꜱᴀᴠᴇʀ ʙᴏᴛ</a> \n๏ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 ➜ ᴘʏᴛʜᴏɴ \n๏ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 ➜ ᴘʏʀᴏɢʀᴀᴍ \n\n☆ 𝗢𝘄𝗻𝗲𝗿 ~ <a href='https://t.me/Itz_Shixnu'>ɪᴛᴢ ꜱʜɪxɴᴜ</a>🥤 \n☆ 𝗝𝗼𝗶𝗻 ~ <a href='https://t.me/Team_Legend_Official'>ᴛᴇᴀᴍ ʟᴇɢᴇɴᴅ ᴏꜰꜰɪᴄɪᴀʟ</a>🥤</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url='https://t.me/Team_Legend_Official'),
                    InlineKeyboardButton("ʙᴀᴄᴋᴜᴘ ᴄʜᴀɴɴᴇʟ", url='https://t.me/TeamLegend_Backup'),
                    ],
                    [
                    InlineKeyboardButton("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴄʜᴀɴɴᴇʟ", url='https://t.me/+Ddg1Q95zBTcxMzhl'),
                    InlineKeyboardButton("ᴜɴʀᴇᴀʟ ʙᴏᴛ", url='https://t.me/unreal_X_Bot'),
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about1":
        await query.message.edit_text(
            text = f"<b>○ᴍʏ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/shubham_X_official'>♡ ꜱʜᴜʙʜᴀᴍ ♡</a> \n○ 🔥Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 🥶sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ  : <a href='https://t.me/itz_sahil_official'>ᴘʀɪᴠᴀᴛᴇ ᴄᴏᴅᴇ</a>\n○ 🥵 ᴅᴏɴᴀᴛᴇ ᴍᴇ : <a href='https://t.me/unreal_X_bot'>ᴄʟɪᴄᴋ ᴍᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏsᴇ ᴍᴇ 🥀", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
