from decouple import config
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

token = config('token')
print(token)

API_KEY = config('API_KEY')
print(API_KEY)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text='Hello, please use /price for using bot')
    await get_price_command(update, context)

async def get_price_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"http://api.navasan.tech/latest/?api_key={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        await context.bot.sendMessage(chat_id=update.effective_chat.id, text=f"""
قیمت خرید دلار : {data['harat_naghdi_sell']['value']} هزار تومن
تاریخ : {data['harat_naghdi_sell']['date']}

قیمت فروش دلار : {data['harat_naghdi_buy']['value']} هزار تومن
تاریخ : {data['harat_naghdi_buy']['date']}
                                        """)

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('price', get_price_command))
    
    app.run_polling()

if __name__=='__main__':
    main()