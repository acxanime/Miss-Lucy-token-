from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5,UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Language : <code>Python3</code></b> 🐍\n<b>○ Version : v1 </b>\n<b>○ Developer : <code>@AcxAnime</code> 😼</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"<b><u>ᴘʀᴇᴍɪᴜᴍ ʙᴇɴɪғɪᴛs ᴀɴᴅ ᴘʀɪᴄᴇs</u> \n\n● ᴅɪʀᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ʟɪɴᴋs\n● ɴᴏ ᴀᴅ ʟɪɴᴋs\n\n● 7 ᴅᴀʏs - ɪɴʀ {PRICE1}\n\n● 1 ᴍᴏɴᴛʜ - ɪɴʀ {PRICE2}\n\n● 3 ᴍᴏɴᴛʜ - ɪɴʀ {PRICE3}\n\n● 6 ᴍᴏɴᴛʜ - ɪɴʀ {PRICE4}\n\n● 12 ᴍᴏɴᴛʜs - ɪɴʀ {PRICE5} \n\n\n💵 UPI ID -  <code>{UPI_ID}</code>\n\n\n📸 QR - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n♻️ If payment is not getting sent on above given QR code then inform admin, he will give you new QR code\n\n\n‼️ Must Send Screenshot after payment\n\nғᴏʀ ᴘᴀʏᴍᴇɴᴛ ᴅᴍ @AcxAnime | @sitaratoons_support</b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("Send Payment Screenshot(ADMIN) 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
            )
