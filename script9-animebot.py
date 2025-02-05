from decouple import config
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

token = config('token')
print(token)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Welcome to anime bot, please use /get_anime to get Baki Hanma anime'
    )

async def get_anime_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
# this is how we make our glassy keys for dowloading episodes :
    keys = []
    
    for i in range(1,24):
        keys.append([
            InlineKeyboardButton(f'Episode {i}', url='https://google.com'),
            InlineKeyboardButton(f'Episode {i+1}', url='https://google.com')
        ])

    reply_markup = InlineKeyboardMarkup(keys)

    with open('/home/mehdi/Downloads/baki.jpg', 'rb') as poster:
        await context.bot.sendPhoto(
            chat_id=update.effective_chat.id,
            photo=poster, # also we cam give a url as a photo like "img_url = https://google.com/baki.jpg" and we do this -> photo = img_url
            caption="""
🥊🔥 BAKI HANMA: THE STRONGEST WARRIOR 🔥🥊

In a world where only the strongest survive, one name stands above all—Baki Hanma! 💪⚡ Raised to surpass his father, Yujiro Hanmay, the most feared creature on Earth, Baki’s journey is a relentless battle for strength, honor, and survival! 🩸👹  

Are you ready to witness the ultimate showdown? ⚡ Let the battle begin! 💥🥊  
""",
reply_markup=reply_markup
)

def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handlers([
        CommandHandler('start', start_command),
        CommandHandler('get_anime', get_anime_command)
    ])
    
    app.run_polling()

if __name__=='__main__':
    main()