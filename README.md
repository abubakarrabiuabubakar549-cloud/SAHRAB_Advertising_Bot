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
app.add_handler(CallbackQueryHandler(payment, "^payment$"))async def payment(update, context):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(
        "💳 BIYAN TALLA\n\n"
        "Bank: Moniepoint MFB\n"
        "Account Name: SAHRAB\n"
        "Account Number: XXXXXXXXXX\n\n"
        "Bayan ka biya, turo screenshot."
    )[InlineKeyboardButton("💳 BIYA TALLA", callback_data="payment")]
async def payment(update, context):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(
        "💳 *BIYAN TALLA*\n\n"
        "Bank: Moniepoint MFB\n"
        "Account Name: Abubakar Rabiu Abubakar\n"
        "Account Number: 6674767017\n\n"
        "Bayan ka biya, danna *Na Biya* ka turo screenshot.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ NA BIYA", callback_data="paid")]
        ])
    )app.add_handler(CallbackQueryHandler(payment, "^payment$"))
[InlineKeyboardButton("💳 BIYA TALLA", callback_data="payment")],async def payment(update, context):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(
        "💳 *BIYAN TALLA*\n\n"
        "Bank: Moniepoint MFB\n"
        "Account Name: Abubakar Rabiu Abubakar\n"
        "Account Number: 6674767017\n\n"
        "Bayan ka biya, danna *NA BIYA* ka turo screenshot.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ NA BIYA", callback_data="paid")]
        ])
    )async def paid(update, context):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(
        "✅ An karɓa.\n\nYanzu turo screenshot na transfer a wannan chat. Zan karɓa domin a tabbatar da biyan kuɗin."
    )

app.add_handler(CallbackQueryHandler(paid, "^paid$"))app.add_handler(CallbackQueryHandler(payment, "^payment$"))
