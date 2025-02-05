from decouple import config
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler, filters

token=config('token')
print(token)

# This is  the normal start command that call menu_command at the end :
async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='welcome to xyz bot, you can buy V2Ray configs from us!',
        )
    await menu_command(update, context)

# This one is our menu and main buttons :
async def menu_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text
    keys = [
        ['Test account 🧪','Buy new service 🔐'],
        ['My services 🛍','Service extension ♻️'],
        ['Guide 📖','Wallet 💰'],
        ['Support ☎️','Advertise us 👨‍👩‍👧‍👧']
    ]
    
    reply_markup = ReplyKeyboardMarkup(keys, resize_keyboard=True)

    await context.bot.sendMessage(
        chat_id=chat_id,
        text='Please choose an option : ',
        reply_markup=reply_markup
    )


async def glassy_buttons_test_buy(update:Update, context:ContextTypes.DEFAULT_TYPE):
    keys = [
        [InlineKeyboardButton('limited | 🇩🇪🇦🇱', callback_data='limited')],
        [InlineKeyboardButton('unlimited | 🇩🇪🇹🇷', callback_data='unlimited')],
        [InlineKeyboardButton('multiserver | 🌐', callback_data='multiserver')],
        [InlineKeyboardButton('gaming | 🇧🇭', callback_data='gaming')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keys)
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Choose an service : ',
        reply_markup=reply_markup
    )


# This one is a echo functoin that handle responsing to menu buttons :
async def response_to_menu(update:Update, context:ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == 'Test account 🧪':
        await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=f'{await glassy_buttons_test_buy(update, context)}'
        )
    elif text == 'Buy new service 🔐':
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id,
            text='glassy_buttons_test_buy'
            # await glassy_buttons_test_buy(update, context)
        )
        if text == 'glassy_buttons_test_buy':
            await glassy_buttons_test_buy(update, context)


async def handle_response(update:Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'limited':
        await query.edit_message_text(text='TEST config - An limited V2Ray config with these locations : 🇩🇪🇦🇱')
    elif query.data == 'unlimited':
        await query.edit_message_text(text='TEST config -An unlimited V2Ray config with these locations : 🇩🇪🇹🇷')
    elif query.data == 'multiserver':
        await query.edit_message_text(text='TEST config -Multiserver config for you :D 🌐')
    elif query.data == 'gaming':
        await query.edit_message_text(text='TEST config -Gaming server for you :D : 🇧🇭')
                

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handlers([
        CommandHandler('start', start_command),
        CommandHandler('menu', menu_command),
        CommandHandler('menu', glassy_buttons_test_buy),
        
        MessageHandler(filters.TEXT & ~filters.COMMAND, response_to_menu),
        
        CallbackQueryHandler(handle_response)
    ])
    
    print('Bot is running...')
    app.run_polling()

main()