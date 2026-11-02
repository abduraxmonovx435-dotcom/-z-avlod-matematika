import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! 👋\n"
        "Z Avlod Matematika botiga xush kelibsiz!\n\n"
        "Matematika videodarslari tez orada!"
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN sozlanmagan!")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
