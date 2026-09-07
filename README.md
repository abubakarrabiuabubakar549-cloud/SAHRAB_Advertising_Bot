

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
CHANNEL_ID = "@SAHRAB_Ads"

def menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 SAKA TALLA", callback_data="ads")],
        [
            InlineKeyboardButton("💰 FARASHI", callback_data="price"),
            InlineKeyboardButton("💳 BIYA", callback_data="pay"),
        ],
        [InlineKeyboardButton("📞 CONTACT ADMIN", url="https://t.me/Excerllency")],
        [InlineKeyboardButton("📺 CHANNEL", url="https://t.me/SAHRAB_Ads")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 SAHRAB Advertising Bot\n\nBarka da zuwa.",
        reply_markup=menu(),
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "ads":
        await q.edit_message_text(
            "📢 Turo mana:\n\n"
            "• Sunan kasuwanci\n"
            "• Rubutun talla\n"
            "• Hoto ko Bidiyo\n"
            "• Bayan ka biya ka turo screenshot.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ BAYA", callback_data="home")]
            ]),
        )

    elif q.data == "price":
        await q.edit_message_text(
            "💰 FARASHIN TALLA\n\n"
            "₦500 — 24 Hours\n"
            "₦1,200 — 3 Days\n"
            "₦2,500 — 7 Days\n"
            "₦5,000 — Pinned Post",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ BAYA", callback_data="home")]
            ]),
        )

    elif q.data == "pay":
        await q.edit_message_text(
            "💳 BIYAN TALLA\n\n"
            "Bank: Moniepoint MFB\n"
            "Account Name: Abubakar Rabiu Abubakar\n"
            "Account Number: 6674767017\n\n"
            "Bayan ka biya, turo screenshot a wannan chat.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ BAYA", callback_data="home")]
            ]),
        )

    elif q.data == "home":
        await q.edit_message_text(
            "🏠 SAHRAB Advertising Bot",
            reply_markup=menu(),
        )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "👨‍💼 Admin Panel\n\n"
        "Ka karɓi odar talla daga nan."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()

if __name__ == "__main__":
    main()
    
