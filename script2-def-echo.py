# So here we going to make a function that reply to our messages 
# also we wanna make a To-Do list function
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

token = config('token')
print(token)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Hello. welcome to 2025 bot (:'
    )

# this is the echo function that echo-back our messages :
'''
async def echo_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=update.message.text,
        reply_to_message_id=update.effective_message.id
    )
'''

# and this one is our todo function that make todo list for us!
# it's an enhanced and useful version of echo function!
async def todo_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    text = update.message.text.split('\n')
    print(text)
    text = '\n\t\t - '.join(text)
    print(text)
    text = f'Your To-Do list is : \n\t\t - {text}'
    print(text)
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=text,
        reply_to_message_id=update.effective_message.id
    )

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handlers([
        CommandHandler('start', start_command),
        MessageHandler(filters.TEXT & ~filters.COMMAND, todo_command)
    ])
    
    app.run_polling()

if __name__=='__main__':
    main()