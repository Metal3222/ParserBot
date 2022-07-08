import logging
from aiogram import Bot, Dispatcher, executor, types
import markup as nav
import sqlite3

# Объект бота
bot = Bot(token="5512113588:AAG8CGXF1HU3bPx9PDB-03yE1-i5_e6_qPs")
# Диспетчер для бота
dp = Dispatcher(bot)
admin_id = 477729063
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Старт приветствие
@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await bot.send_animation(message.from_user.id, types.InputFile("images/welcome.gif"))
    await message.reply(f"Добрый день, {message.from_user.first_name}. Я подберу для тебя необходимые товары!",
                        reply_markup=nav.mainMenu)


# Обработчик данных

@dp.message_handler()
async def bot_message(message: types.Message):
    # Меню поиск
    if message.text == "Поиск":
        await bot.send_message(message.from_user.id, "Перевожу тебя к поиску",
                               reply_markup=nav.workMenu)
    if message.text == "Сортировка":
        await bot.send_message(message.from_user.id, "Перевожу тебя к сортировке",
                               reply_markup=nav.workMenu)
    if message.text == "Что-то еще":
        await bot.send_message(message.from_user.id, "Что-то еще",
                               reply_markup=nav.workMenu)

    # Меню пользователя
    if message.text == "Меню пользователя":
        await bot.send_message(message.from_user.id, "Перевожу тебя в меню пользователя",
                               reply_markup=nav.userMenu)
    if message.text == "Статус":
        await bot.send_message(message.from_user.id, "Перевожу тебя к сортировке",
                               reply_markup=nav.userMenu)
    if message.text == "Купить подписку":
        await bot.send_message(message.from_user.id, "Покупай",
                               reply_markup=nav.userMenu)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

