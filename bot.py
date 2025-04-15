import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from filters import is_spam

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WARNINGS = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    user_id = message.from_user.id
    if is_spam(message.text):
        await message.delete()
        WARNINGS[user_id] = WARNINGS.get(user_id, 0) + 1
        warning_count = WARNINGS[user_id]
        await message.reply_text(f"⚠️ Bu guruhda reklama taqiqlangan! Ogohlantirishlar soni: {warning_count}")

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
