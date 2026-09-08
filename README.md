app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("channel", channel))async def price(update, context):
    await update.message.reply_text(
        "💰 FARASHI\n\n"
        "₦500 - 24 Hours\n"
        "₦1,200 - 3 Days\n"
        "₦2,500 - 7 Days\n"
        "₦5,000 - Pinned Post"
    )

async def contact(update, context):
    await update.message.reply_text(
        "📞 Yi magana da Admin:",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("💬 BUƊE ADMIN", url="https://t.me/Excerllency")
        ]])
    )

async def channel(update, context):
    await update.message.reply_text(
        "📺 Shiga channel:",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🚀 SAHRAB ADS", url="https://t.me/SAHRAB_Ads")
        ]])
    )import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 SAKA TALLA", callback_data="ads")],
        [
            InlineKeyboardButton("💰 FARASHI", callback_data="price"),
            InlineKeyboardButton("💳 BIYA", callback_data="pay"),
        ],
        [InlineKeyboardButton("📞 CONTACT ADMIN", url="https://t.me/Excerllency")],
        [InlineKeyboardButton("📺 SHIGA CHANNEL", url="https://t.me/SAHRAB_Ads")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📢 *SAHRAB Advertising Bot*\n\n"
        "Barka da zuwa.\n"
        "Zaɓi abin da kake so."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "👨‍💼 *ADMIN PANEL*\n\n"
        "Bot yana aiki.",
        parse_mode="Markdown",
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "ads":
        await q.edit_message_text(
            "📢 *SAKA TALLA*\n\n"
            "Ka turo:\n"
            "• Sunan kasuwanci\n"
            "• Rubutun talla\n"
            "• Hoto ko Bidiyo\n\n"
            "Bayan ka biya ka turo screenshot.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ BAYA", callback_data="home")]
            ]),
        )

    elif q.data == "price":
        await q.edit_message_text(
            "💰 *FARASHIN TALLA*\n\n"
            "• ₦500 — 24 Hours\n"
            "• ₦1,200 — 3 Days\n"
            "• ₦2,500 — 7 Days\n"
            "• ₦5,000 — Pinned Post",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ BAYA", callback_data="home")]
            ]),
        )

    elif q.data == "pay":
        await q.edit_message_text(
            "💳 *BIYAN TALLA*\n\n"
            "Bank: Moniepoint MFB\n"
            "Account Name: Abubakar Rabiu Abubakar\n"
            "Account Number: 6674767017\n\n"
            "Bayan ka biya ka turo screenshot a wannan chat.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ BAYA", callback_data="home")]
            ]),
        )

    elif q.data == "home":
        await q.edit_message_text(
            "🏠 *SAHRAB Advertising Bot*",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CallbackQueryHandler(buttons))

    print("SAHRAB Advertising Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
async def price(update, context):
    await update.message.reply_text(
        "💰 FARASHIN TALLA\n\n"
        "⭐ Basic – ₦100\n"
        "⭐ Standard – ₦500\n"
        "⭐ Premium – ₦1000"
    )

async def contact(update, context):
    await update.message.reply_text(
        "📞 Yi magana da Admin:",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("💬 BUƊE ADMIN", url="https://t.me/Excerllency")
        ]])
    )

async def channel(update, context):
    await update.message.reply_text(
        "📺 Shiga Channel:",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🚀 SAHRAB ADS", url="https://t.me/SAHRAB_Ads")
        ]])
    )app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("channel", channel))
app.add_handler(CommandHandler("admin", admin))
app.add_handler(CallbackQueryHandler(buttons))
