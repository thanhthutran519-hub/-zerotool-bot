from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8545174105:AAHhaC_JUIZ6V_4CFzyc7JStkb87zfUO_II"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào! Bot đang hoạt động.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
