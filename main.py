from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Инициализация бота (замените токен на свой!)
bot = Bot(token="7196195659:AAEEigdMe0HR8u9Qp_1vq1VSFRGlVH5zy3U")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "⚔️ Добро пожаловать в Tea Clicker!\n"
        "Нажми кнопку ниже, чтобы начать игру!",
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[
            types.InlineKeyboardButton(
                text="🎮 Открыть игру",
                web_app=types.WebAppInfo(url="https://hovi11.github.io/tea_clicker/")
            )
        ]])
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())