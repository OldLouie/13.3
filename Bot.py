import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="HTTP API")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.!')


# Хэндлер на команду сообщение
#@dp.message()
#async def cmd_txt(message: types.Message):
#    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Хэндлер на команду сообщение
@dp.message()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
