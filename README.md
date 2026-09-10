def menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 POST AN AD", callback_data="ads")],
        [
            InlineKeyboardButton("💰 PRICING", callback_data="price"),
            InlineKeyboardButton("💳 PAY NOW", callback_data="pay")
        ],
        [InlineKeyboardButton("📞 CONTACT ADMIN", callback_data="contact")],
        [InlineKeyboardButton("📺 JOIN CHANNEL", callback_data="channel")]
    ])async def start(update, context):
    await update.message.reply_text(
        "🚀 *Welcome to SAHRAB Advertising Bot!*\n\n"
        "Promote your business, products, services, or Telegram channel.\n\n"
        "Choose an option below.",
        parse_mode="Markdown",
        reply_markup=menu()
    )elif q.data == "ads":
    await q.edit_message_text(
        "📢 *POST AN AD*\n\n"
        "Please send:\n"
        "• Business name\n"
        "• Ad description\n"
        "• Photo or video\n"
        "• Payment screenshot after payment.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ BACK", callback_data="home")]
        ])
    )elif q.data == "price":
    await q.edit_message_text(
        "💰 *ADVERTISING PRICES*\n\n"
        "⭐ Basic — ₦100\n"
        "⭐ Standard — ₦500\n"
        "⭐ Premium — ₦1,000\n"
        "⭐ Pinned Post — ₦5,000",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ BACK", callback_data="home")]
        ])
    )elif q.data == "pay":
    await q.edit_message_text(
        "💳 *PAYMENT DETAILS*\n\n"
        "Bank: Moniepoint MFB\n"
        "Account Name: Abubakar Rabiu Abubakar\n"
        "Account Number: 6674767017\n\n"
        "After payment, send your payment screenshot here.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ BACK", callback_data="home")]
        ])
    )elif q.data == "contact":
    await q.edit_message_text(
        "📞 Contact the Admin using the button below.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("💬 OPEN ADMIN", url="https://t.me/Excerllency")],
            [InlineKeyboardButton("⬅️ BACK", callback_data="home")]
        ])
    )elif q.data == "channel":
    await q.edit_message_text(
        "📺 Join our official channel.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🚀 JOIN CHANNEL", url="https://t.me/SAHRAB_Ads")],
            [InlineKeyboardButton("⬅️ BACK", callback_data="home")]
        ])
    )async def admin(update, context):
    if update.effective_user.id not in ADMIN_IDS:
        return

    await update.message.reply_text(
        "👨‍💼 *Admin Panel*\n\n"
        "Welcome, Admin.",
        parse_mode="Markdown"
    )
