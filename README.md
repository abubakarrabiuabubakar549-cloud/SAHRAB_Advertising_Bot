💰 FARASHIN TALLA – SAHRAB Advertising Bot

- ₦500 – 24 Hours
- ₦1,200 – 3 Days
- ₦2,500 – 7 Days
- ₦5,000 – Pinned Post

Danna SAKA TALLA domin turo tallarka.
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📢 Business Ads", callback_data="business")],
        [InlineKeyboardButton("🛍 Product Promotion", callback_data="product")],
        [InlineKeyboardButton("📣 Telegram Channel", callback_data="channel")],
        [InlineKeyboardButton("📞 Tuntubi Admin", url="https://t.me/USERNAME_DINKA")]
    ]

    await update.message.reply_text(
        "👋 Barka da zuwa SAHRAB Advertising Bot.\n\nZaɓi irin tallar da kake so:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
