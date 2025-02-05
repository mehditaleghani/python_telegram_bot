# in this section we just gonna make a function that works for /start of telegram bot
# so we go :
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

token = config('token')
print(token)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Hello Boss'
    )

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler('start', start_command))
    
    app.run_polling()

if __name__=='__main__':
    main()