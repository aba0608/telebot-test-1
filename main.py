import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен бота - укажи в Render в переменных окружения BOT_TOKEN
TOKEN = os.getenv("7849157703:AAEyK4jmuvCync2ZcHvi6_W5HQCYZMCEZMk")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Тексты сообщений
FIRST_MESSAGE = "Привет! Вот видео: https://youtube.com/..."
SECOND_MESSAGE = "А вот анкета: https://example.com/anketa"
THIRD_MESSAGE = "Подпишись на наш канал: https://t.me/your_channel"
FOURTH_MESSAGE = "Напиши нам: https://t.me/your_account"

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    await message.answer(FIRST_MESSAGE)

    # Запускаем цепочку сообщений (асинхронно, чтобы не блокировать бота)
    asyncio.create_task(send_sequence(user_id))

async def send_sequence(user_id: int):
    await asyncio.sleep(7 * 60)  # 7 минут
    await bot.send_message(user_id, SECOND_MESSAGE)

    await asyncio.sleep(10 * 60)  # 10 минут
    await bot.send_message(user_id, THIRD_MESSAGE)

    await asyncio.sleep(12 * 60 * 60)  # 12 часов
    await bot.send_message(user_id, FOURTH_MESSAGE)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
