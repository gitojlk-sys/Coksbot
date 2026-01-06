import os
from telegram.ext import Application, MessageHandler, filters

async def reply(update, context):
    await update.message.reply_text("Bot hidup 🔥")

app = Application.builder().token(
    os.getenv("BOT_TOKEN")
).build()

app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()