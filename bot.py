import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler

# Токен берем из переменной окружения (БЕЗОПАСНО!)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context):
    """Ответ на команду /start"""
    await update.message.reply_text("Привет! 👋 Я бот, который работает на Render.com")

async def main():
    """Запуск бота"""
    if not BOT_TOKEN:
        print("Ошибка: BOT_TOKEN не найден в переменных окружения")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Бот запущен и работает...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
