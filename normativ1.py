import asyncio
import psycopg2
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = '8199528786:AAGNvFfO_r8zgdWNSZQi3gmV1GpdrYpNRMQ'


# Подключение к базе
conn = psycopg2.connect(
    dbname="myproject",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

bot = Bot(token=TOKEN)
dp = Dispatcher()


# 📌 Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    cursor.execute(
        "INSERT INTO core_botuser (user_id, username, full_name, created_at) "
        "VALUES (%s, %s, %s, NOW()) "
        "ON CONFLICT (user_id) DO NOTHING;",
        (user_id, username, full_name)
    )
    conn.commit()

    await message.answer("Привет! Ты добавлен в базу ✅")


# 📌 Команда /users (получение из БД)
@dp.message(Command("users"))
async def get_users(message: types.Message):
    cursor.execute("SELECT username, full_name FROM core_botuser ORDER BY created_at DESC;")
    rows = cursor.fetchall()

    if not rows:
        await message.answer("Нет пользователей в базе ❌")
    else:
        text = "\n".join([f"@{u} ({f})" for u, f in rows if u])
        await message.answer(f"👥 Пользователи:\n{text}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
