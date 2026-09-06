import os, sqlite3, logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, ContextTypes, PreCheckoutQueryHandler, filters

TOKEN = os.getenv('BOT_TOKEN','').strip()
ADMIN_ID = int(os.getenv('ADMIN_ID','0'))
DB='ads.db'
NAME, TEXT, MEDIA = range(3)
PRICES={'basic':100,'featured':250,'premium':500}
logging.basicConfig(level=logging.INFO)

def db():
    c=sqlite3.connect(DB)
    c.execute('''CREATE TABLE IF NOT EXISTS ads (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER,username TEXT,business TEXT,ad_text TEXT,media_file_id TEXT,media_type TEXT,package TEXT,stars INTEGER,status TEXT DEFAULT 'pending',created_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.commit(); return c

def menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton('📢 SAKA TALLA',callback_data='advertise')],[InlineKeyboardButton('💰 FARASHIN TALLA',callback_data='prices')],[InlineKeyboardButton('📦 AYYUKANMU',callback_data='services')],[InlineKeyboardButton('📞 TUNTUƁI ADMIN',callback_data='contact')]])

async def start(u,c):
    await u.message.reply_text('📢 *SAHRAB Advertising Bot*\n\nMuna taimaka maka ka tallata kasuwanci, kaya, services da Telegram channels.\n\nZaɓi abin da kake so:',parse_mode='Markdown',reply_markup=menu())
async def prices(u,c):
    q=u.callback_query; await q.answer()
    kb=InlineKeyboardMarkup([[InlineKeyboardButton('🥉 BASIC — 100 ⭐',callback_data='choose_basic')],[InlineKeyboardButton('🥈 FEATURED — 250 ⭐',callback_data='choose_featured')],[InlineKeyboardButton('🥇 PREMIUM — 500 ⭐',callback_data='choose_premium')],[InlineKeyboardButton('⬅️ BAYA',callback_data='home')]])
    await q.edit_message_text('💰 *Farashin Talla*\n\n🥉 Basic — 100 ⭐\n🥈 Featured — 250 ⭐\n🥇 Premium — 500 ⭐',parse_mode='Markdown',reply_markup=kb)
async def services(u,c):
    q=u.callback_query; await q.answer(); await q.edit_message_text('📦 *Ayyukanmu*\n\n• Tallan kasuwanci\n• Tallan kaya\n• Tallan services\n• Tallan Telegram channels',parse_mode='Markdown',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅️ BAYA',callback_data='home')]]))
async def contact(u,c):
    q=u.callback_query; await q.answer(); await q.edit_message_text('📞 *Tuntuɓi Admin*\n\nAika saƙo zuwa admin domin taimako.',parse_mode='Markdown',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅️ BAYA',callback_data='home')]]))
async def advertise(u,c):
    q=u.callback_query; await q.answer(); c.user_data.clear(); await q.edit_message_text('📢 *SAKA TALLA*\n\nMataki 1/4: Rubuta sunan kasuwancinka.',parse_mode='Markdown'); return NAME
async def get_name(u,c):
    c.user_data['business']=u.message.text[:100]; await u.message.reply_text('Mataki 2/4: Rubuta rubutun tallanka.'); return TEXT
async def get_text(u,c):
    c.user_data['ad_text']=u.message.text[:2000]; await u.message.reply_text('Mataki 3/4: Turo hoton/video na tallanka. Idan babu, rubuta `babu`.'); return MEDIA
async def get_media(u,c):
    if u.message.photo: c.user_data.update(media_file_id=u.message.photo[-1].file_id,media_type='photo')
    elif u.message.video: c.user_data.update(media_file_id=u.message.video.file_id,media_type='video')
    else: c.user_data.update(media_file_id='',media_type='')
    kb=InlineKeyboardMarkup([[InlineKeyboardButton('🥉 BASIC — 100 ⭐',callback_data='choose_basic')],[InlineKeyboardButton('🥈 FEATURED — 250 ⭐',callback_data='choose_featured')],[InlineKeyboardButton('🥇 PREMIUM — 500 ⭐',callback_data='choose_premium')]])
    await u.message.reply_text('Mataki 4/4: Zaɓi package ɗin tallanka:',reply_markup=kb); return ConversationHandler.END
async def choose(u,c):
    q=u.callback_query; await q.answer(); package=q.data.replace('choose_',''); stars=PRICES[package]
    c.user_data['package']=package
    conn=db(); cur=conn.execute('INSERT INTO ads(user_id,username,business,ad_text,media_file_id,media_type,package,stars) VALUES(?,?,?,?,?,?,?,?)',(q.from_user.id,q.from_user.username or '',c.user_data.get('business',''),c.user_data.get('ad_text',''),c.user_data.get('media_file_id',''),c.user_data.get('media_type',''),package,stars)); ad_id=cur.lastrowid; conn.commit(); conn.close()
    await q.edit_message_text(f'🧾 *Talla #{ad_id}*\n\nKasuwanci: {c.user_data.get("business")}\nPackage: {package.upper()}\nFarashi: {stars} ⭐',parse_mode='Markdown',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('💳 PAY NOW',callback_data=f'pay_{ad_id}')]]))
async def pay(u,c):
    q=u.callback_query; await q.answer(); ad_id=int(q.data.split('_')[1]); conn=db(); row=conn.execute('SELECT business,package,stars FROM ads WHERE id=? AND user_id=?',(ad_id,q.from_user.id)).fetchone(); conn.close()
    if not row: return await q.message.reply_text('Ba a sami tallan ba.')
    business,package,stars=row
    await c.bot.send_invoice(q.from_user.id,f'SAHRAB Ads — {package.upper()}',f'Tallan {business} a SAHRAB Advertising.',f'ad:{ad_id}','', 'XTR',[LabeledPrice('Advertising',stars)])
async def precheckout(u,c): await u.pre_checkout_query.answer(ok=True)
async def paid(u,c):
    p=u.message.successful_payment; ad_id=int(p.invoice_payload.split(':')[1]); conn=db(); row=conn.execute('SELECT * FROM ads WHERE id=?',(ad_id,)).fetchone(); conn.execute("UPDATE ads SET status='paid' WHERE id=?",(ad_id,)); conn.commit(); conn.close()
    if ADMIN_ID and row:
        await c.bot.send_message(ADMIN_ID,f'💰 AN BIYA TALLA #{ad_id}\nKasuwanci: {row[3]}\nPackage: {row[7]}\nStars: {row[8]}\nUsername: @{row[2] or "babu"}')
        caption=f'📢 TALLA #{ad_id}\n\n{row[4]}'
        if row[6]=='photo' and row[5]: await c.bot.send_photo(ADMIN_ID,row[5],caption=caption)
        elif row[6]=='video' and row[5]: await c.bot.send_video(ADMIN_ID,row[5],caption=caption)
        else: await c.bot.send_message(ADMIN_ID,caption)
    await u.message.reply_text('✅ An karɓi biyan kuɗinka! Tallanka yana jiran approval na admin.')
async def home(u,c):
    q=u.callback_query; await q.answer(); await q.edit_message_text('🏠 *SAHRAB Advertising Bot*\n\nZaɓi service:',parse_mode='Markdown',reply_markup=menu())

async def cancel(u,c): await u.message.reply_text('An soke aikin.'); return ConversationHandler.END

def main():
    if not TOKEN: raise RuntimeError('BOT_TOKEN is missing')
    db(); app=Application.builder().token(TOKEN).build()
    conv=ConversationHandler(entry_points=[CallbackQueryHandler(advertise,'^advertise$')],states={NAME:[MessageHandler(filters.TEXT & ~filters.COMMAND,get_name)],TEXT:[MessageHandler(filters.TEXT & ~filters.COMMAND,get_text)],MEDIA:[MessageHandler(filters.PHOTO | filters.VIDEO | (filters.TEXT & ~filters.COMMAND),get_media)]},fallbacks=[CommandHandler('cancel',cancel)])
    app.add_handler(CommandHandler('start',start)); app.add_handler(CallbackQueryHandler(prices,'^prices$')); app.add_handler(CallbackQueryHandler(services,'^services$')); app.add_handler(CallbackQueryHandler(contact,'^contact$')); app.add_handler(CallbackQueryHandler(home,'^home$')); app.add_handler(CallbackQueryHandler(choose,'^choose_(basic|featured|premium)$')); app.add_handler(CallbackQueryHandler(pay,r'^pay_\d+$')); app.add_handler(conv); app.add_handler(PreCheckoutQueryHandler(precheckout)); app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT,paid)); app.run_polling()
if __name__=='__main__': main()
