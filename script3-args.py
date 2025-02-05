# this is a command `/start` and these are arguments : `/start arg1 ARG2`
# we are gonna see how to use them and what can we do with args :
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

token = config('token')
print(token)

# I want you to run the script and enter this command `/start arg1 ARG2`
async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    args = context.args
    print(args) # as you see we have a list of arguments named args
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='''Welcome to 2025 bot
please enter this command `/start arg1 ARG2` and than check your terminal please'''
    )

# imagine we have a database that contain usernames and phone numbers, we want a function
# that add users and phone numbers to that database, in this example we use a simple
# dict and list as our database but in real applications i think it's better to use SQL

database = {
    'id':[],
    'name':[],
    'phone': [],
}

async def adduser_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    args = context.args
    user_id = update.effective_user.id

    if user_id in database['id']:
        await context.bot.sendMessage(chat_id=update.effective_chat.id, text='You made your account before ... sorry ): ')
    elif len(args) > 2:
        await context.bot.sendMessage(chat_id=update.effective_chat.id, text='To many arguments please enter a username and a phonenumber')
    elif len(args) < 2:
        await context.bot.sendMessage(chat_id=update.effective_chat.id, text='please enter a username and a phonenumber')
    else:
        await context.bot.sendMessage(chat_id=update.effective_chat.id, text=f'username {args[0]} and phonenumber {args[1]} added to database')
        database['id'].append(user_id)
        print(args[0], args[1])

print(database['id'])
print(database['name'])
print(database['phone'])

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handlers([
        CommandHandler('start', start_command),
        CommandHandler('adduser', adduser_command)
    ])
    
    app.run_polling()
    
if __name__=='__main__':
    main()