
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes,CommandHandler
import os 
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig (
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= "Я бот, который помогает вырбать услуги и также записаться на сеанс")

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('token')).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()




