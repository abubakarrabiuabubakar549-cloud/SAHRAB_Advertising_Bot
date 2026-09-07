CHANNEL_ID = "@SAHRAB_Ads"CHANNEL_ID = os.getenv("CHANNEL_ID", "").strip()💰 FARASHIN TALLA – SAHRAB Advertising Bot

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
await q.edit_message_text(
    "📢 *SAKA TALLA*\n\n"
    "1. Rubuta sunan kasuwancinka.\n"
    "2. Rubuta bayanin tallarka.\n"
    "3. Turo hoto ko bidiyo.\n"
    "4. Zaɓi package.\n\n"
    "Za a aika mini kai tsaye domin approval.",
    parse_mode="Markdown"
)await q.edit_message_text("📢 *SAKA TALLA*\n\nMataki 1/4: Rubuta *sunan kasuwancinka*.", parse_mode="Markdown")
