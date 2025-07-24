from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
import asyncio

# ⬛ 1. Umgebungsvariablen laden
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

# ⬛ 2. Bot & Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ⬛ 3. /start-Befehl mit Sniper-Button
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🚀 Sniper Alpha", callback_data="sniper_alpha"))
    await message.answer("👋 Willkommen im CryptoTec Bot!\nWähle eine Option:", reply_markup=keyboard)

# ⬛ 4. Button-Reaktion: Sniper Alpha Status
@dp.callback_query_handler(lambda c: c.data == 'sniper_alpha')
async def sniper_status_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
        "🧠 *SniperBot Status*\n"
        "Letzter Check: 24.07.2025, 03:33 Uhr\n"
        "Status: ✅ *Aktiv*",
        parse_mode="Markdown")

# ⬛ 5. Sniper Loop
async def sniper_loop():
    while True:
        print("[SNIPER] Suche nach Token-Launches...")
        await asyncio.sleep(5)

# ⬛ 6. Startup-Hook: Sniper starten
async def on_startup(dp):
    asyncio.create_task(sniper_loop())

# ⬛ 7. Bot starten
if __name__ == '__main__':
    print("[SYSTEM] Starte Bot...")
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)