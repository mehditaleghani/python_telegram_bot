import requests
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

token = config('token')
print(token)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Hello welcome to joke bot, use /joke and i\'ll send you a joke :D'
    )

async def joke_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    response = requests.get('https://v2.jokeapi.dev/joke/Dark')
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            await context.bot.sendMessage(
                chat_id=update.effective_chat.id,
                text=data['joke']
            )
        elif data['type'] == 'twopart':
            await context.bot.sendMessage(chat_id=update.effective_chat.id, text=data['setup'] + '\n' + data['delivery'])            
    elif response.status_code != 200:
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id,
            text='Sorry I don\'t have any jokes for now ... try again'
        )
    
def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handlers([
        CommandHandler('start', start_command),
        CommandHandler('joke', joke_command)
    ])
    
    app.run_polling()

if __name__=='__main__':
    main()