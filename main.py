from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8545174105:AAHuuyn8xUO7R2I1-A6fqQgZDMzxsQtnSzg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào! Bot đang hoạt động.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
