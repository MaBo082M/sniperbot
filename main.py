import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("📊 Dashboard öffnen", web_app=WebAppInfo(url="https://cryptoteccontrol.up.railway.app/dashboard"))
    )
    await message.answer("Willkommen bei CryptoTecControl 👇", reply_markup=keyboard)

async def sniper_loop():
    print(f"[SNIPER] Wallet aktiv: {WALLET_ADDRESS}")
    while True:
        print("[SNIPER] Suche nach Token-Launches ...")
        await asyncio.sleep(5)

async def main():
    print("[SYSTEM] Starte SniperLoop ...")
    asyncio.create_task(sniper_loop())
    
    print("[SYSTEM] Starte TelegramBot...")
    await dp.start_polling()

if __name__ == "__main__":
    print("[SYSTEM] Initialisiere Bot...")
    asyncio.run(main())
