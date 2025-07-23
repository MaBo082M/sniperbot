import os
import time
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import asyncio

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ✅ /start Handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="📊 Dashboard öffnen",
            web_app=types.WebAppInfo(url="https://cryptoteccontrol.up.railway.app/dashboard")
        )
    )
    await message.answer("Willkommen bei CryptoTecControl! 👇", reply_markup=keyboard)

# ✅ SniperLoop als Hintergrundtask
async def sniper_loop():
    print(f"[SNIPER] Wallet aktiv: {WALLET_ADDRESS}")
    while True:
        print("[SNIPER] Suche nach Token-Launches …")
        await asyncio.sleep(5)

# ✅ Start Bot und Sniper parallel
async def main():
    asyncio.create_task(sniper_loop())
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())