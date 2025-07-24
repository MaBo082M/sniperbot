import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def start_handler(message: types.Message):
    await message.answer("✅ CryptoTec Bot ist aktiv!")

async def sniper_loop():
    while True:
        print("[SNIPER] Aktiver Check...")
        await asyncio.sleep(5)

async def main():
    print("[SYSTEM] Starte Bot...")
    asyncio.create_task(sniper_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
