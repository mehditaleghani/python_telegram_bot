from decouple import config
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

token = config('token')
print(token)

# this is not a keyboard button it's just a normal button that users will choose an
# option and all options will disapier for example we ask user for what episode of
# series user wants :D
# or we can force them to join some channels , if they joined the channels bot will
# send them some photos else nothing :D
async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    keys = [
        [
            # and we learn some new stuff here :
            InlineKeyboardButton('option1', callback_data='opt1'),
            InlineKeyboardButton('option2', callback_data='opt2'),
            # callback data is the backend data that our code gonna recieve as user choose
            # and this one let us to redirect users :
            InlineKeyboardButton('Join channel 1 to see photos :D', url='google.com')
        ],
        [
            # this list goes to a new row just like replykeyboardmarkup :D
            InlineKeyboardButton('final_channel', url='yahoo.com')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keys)

    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Choose an option : ',
        reply_to_message_id=update.effective_message.id,
        reply_markup=reply_markup
    )

# and we need this function for butons like option1 and option2 :
async def handle_response(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    
    if update.callback_query.data == 'opt1':
        await update.callback_query.edit_message_text('You choosed option 1')
    elif update.callback_query.data == 'opt2':
        await update.callback_query.edit_message_text('You choosed option 2')

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler('start', start_command)),
    
    # we also need to add this handler to handle them
    app.add_handler(CallbackQueryHandler(handle_response))
    
    app.run_polling()
    
if __name__=='__main__':
    main()