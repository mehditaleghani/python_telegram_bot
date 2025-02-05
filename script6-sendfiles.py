from decouple import config
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

token = config('token')
print(token)

async def start_command(update:Update, context):
    await update.message.reply_text('''
Hello this is TheFirst2025_bot
for now it have 3 features 
use /menu to see all features
''')

async def give_me_photo(update:Update, context):
    with open ('/home/mehdi/Pictures/Screenshots/morty.png' , 'rb') as photo:
        await update.message.reply_photo(photo, caption='here\'s your photo')

async def give_me_music(update:Update, context):
    with open ('/home/mehdi/Music/Chub1na.mp3', 'rb') as  music:
        await update.message.reply_audio(music, caption='Here\'s your audio')

async def give_me_textfile(update:Update, context):
    with open ('/home/mehdi/Desktop/To-Buy.txt', 'rb') as textfile:
        await update.message.reply_document(textfile, caption='Here\'s your text file')

async def menu_command(update:Update, context):
    keyboard = [
        ['give_me_photo', 'give_me_music', 'give_me_textfile'],
        ['Exit']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        'choose a feature to test :',
        reply_markup=reply_markup,
    )

async def response_menu_command(update:Update, context):
    text = update.message.text
    if text == 'give_me_photo':
        await give_me_photo(update, context)
    elif text == 'give_me_music':
        await give_me_music(update, context)
    elif text == 'give_me_textfile':
        await give_me_textfile(update, context)
        
def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('menu', menu_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, response_menu_command))

    app.run_polling()

if __name__=='__main__':
    main()