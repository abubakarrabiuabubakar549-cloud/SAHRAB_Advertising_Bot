@bot.callback_query_handler(func=lambda call: True)
def buttons(call):
    if call.data == "submit_ad":
        bot.send_message(call.message.chat.id,
            "📢 Turo hoton tallarka tare da rubutu. Admin zai karɓa.")

    elif call.data == "pricing":
        bot.send_message(call.message.chat.id,
            "💰 Farashin Talla:\nBusiness - ₦500\nProduct - ₦300\nChannel - ₦200")

    elif call.data == "packages":
        bot.send_message(call.message.chat.id,
            "📦 Kunshinmu:\n• Business Ads\n• Product Promotion\n• Telegram Channel Promotion")

    elif call.data == "contact_admin":
        bot.send_message(call.message.chat.id,
            "📞 Tuntuɓi Admin: @SAHRAB_Advertising")
