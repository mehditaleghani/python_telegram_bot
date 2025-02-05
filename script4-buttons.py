from decouple import config
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

token = config('token')
print(token)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    # so these are our keyboard buttons :
    keys = [
        ['option-1', 'option-2'],
        ['Exit']
    ]
    
    # and here we make them and give them style :
    reply_markup = ReplyKeyboardMarkup(keyboard=keys) # this is the basic form of RKM, we must give a list of keys to this class
    reply_markup = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True) # for better button size
    '''
    reply_markup = ReplyKeyboardMarkup(keyboard=keys, one_time_keyboard=True) # this one exit us from keybvoard after an option selection
    reply_markup = ReplyKeyboardMarkup(keyboard=keys, input_field_placeholder='Choose an option') # This one is a place holder
    '''
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Hello please choose an option :',
        # and with this line we enable it :
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handlers([
        CommandHandler('start', start_command)
    ])
    
    app.run_polling()

if __name__=='__main__':
    main()