import os
import django
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from asgiref.sync import sync_to_async

# --- Настройка Django ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytg.settings")
django.setup()

from core.models import BotUser


# --- Настройка бота ---
TOKEN = '8199528786:AAGNvFfO_r8zgdWNSZQi3gmV1GpdrYpNRMQ'
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Сохранение пользователя ---
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    # ORM через sync_to_async
    await sync_to_async(BotUser.objects.get_or_create)(
        user_id=user_id,
        defaults={"username": username, "full_name": full_name},
    )

    await message.answer("👋 Привет! Ты зарегистрирован в базе ✅")

# --- Вывод списка пользователей ---
@dp.message(Command("users"))
async def users_cmd(message: types.Message):
    users = await sync_to_async(list)(BotUser.objects.all().order_by("-created_at"))
    if not users:
        await message.answer("❌ В базе пока нет пользователей")
        return

    text = "\n".join([f"@{u.username or '-'} ({u.full_name})" for u in users])
    await message.answer(f"👥 Пользователи:\n{text}")

# --- Личная информация ---
@dp.message(Command("info"))
async def info_cmd(message: types.Message):
    try:
        user = await sync_to_async(BotUser.objects.get)(user_id=message.from_user.id)
        await message.answer(
            f"📝 Твои данные:\n\n"
            f"ID: {user.user_id}\n"
            f"Имя: {user.full_name}\n"
            f"Username: @{user.username}\n"
            f"Дата регистрации: {user.created_at}"
        )
    except BotUser.DoesNotExist:
        await message.answer("❌ Ты ещё не зарегистрирован")

# --- Запуск бота ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
