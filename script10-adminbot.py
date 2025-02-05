from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

token = config('token')
print(token)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='''
Hello welcome to 2025 bot, I can forward some messages for you
for example I can send 10 anime episodes to a specefiv channel
and after it when you want anime episodes I just forward them to you.
or I can forward a specefic message to some telegram channel each
time you run me :D and these stuff ...
use /forward_message command to see :D
''')

#forward message consepct :
async def forward_message_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.forwardMessage(
        # you can give the target channel chat_id, and it will send the message to target chat_id
        # in this section we wanna send message to our self chat with bot so we use "update.effective_chat.id"
        # but we can use something like "@imtestingthefirst2025_bot" as chat_id and message will be send to "https://t.me/programmering_group"
        chat_id=update.effective_chat.id,
        # now you need a channel that contain messages that you wanna forward, and you give the channel address
        # remember that channel should be public else you need the privet address of the channel
        # tip : bot should be Admin of the channel that you wanna forward message from it :D
        from_chat_id='@imtestingthefirst2025_bot',
        # when you copy a message form a channel it have a link like this : "https://t.me/imtestingthefirst2025_bot/2"
        # you need the last part in this example it's "2"
        message_id=2
        # and this send you the message with id of "2" from "programming_group" to you :D
    )
    
#sending message to channels :
async def send_message_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id='@imtestingthefirst2025_bot',
        text='I\'m @TheFirst2025_bot and I can send message to channels that im admin of them'
    )
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Message sent to @imtestingthefirst2025_bot'
    )

#edit message consepct :
async def edit_message_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.edit_message_text(
        chat_id='@imtestingthefirst2025_bot',
        text='Hello world I\'m the new text',
        message_id=3
    )
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text='Message edited succesfully :D'
    )

# making a timer :
# pip install python-telegram-bot[job-queue]
'''
async def automation(update:Update, contex:ContextTypes.DEFAULT_TYPE):
    await contex.job_queue.run...
'''

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handlers([
        CommandHandler('start', start_command),
        CommandHandler('forward_message', forward_message_command),
        CommandHandler('send_message', send_message_command),
        CommandHandler('edit_message', edit_message_command)
    ])

    app.run_polling()
    
if __name__=='__main__':
    main()