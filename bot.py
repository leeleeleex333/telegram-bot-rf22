from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 欢迎文案
    caption = (
        "🎰 *Selamat Datang ke RoyalFlash22* 🎰\n\n"
        "🔒 *Trusted Platform & Paling Selamat*\n"
        "🎰 Mega888, Pussy888, Playtech, Live22, Pragmatic Play, Jili, XE88, 918KissH5\n\n"
        "🔥 *Promotion* 🔥\n"
        "📌 *WLC Bonus 150% (3 Kali)* 🔥\n"
        "🥇 *New Register Free 30 (Tanpa deposit)* 🔥\n"
        "🥇 *Free Credit 365 Hari* 🔥\n"
        "🥈 *Free Share Bonus* 🔥\n"
        "🥉 *2Days Rebate Kaw Kaw* 🔥"
    )

    # 注册按钮 + 客服按钮
    keyboard = [
        [InlineKeyboardButton("🔥 Register Now", url="https://royalflash22.net/RFRF22BOT")],
        [InlineKeyboardButton("📞 Telegram Customer Service", url="https://t.me/RF22CS1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 发送新图片 + 信息 + 按钮
    with open("bot photo 1.png", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

# 启动 bot
if __name__ == "__main__":
    app = ApplicationBuilder().token("7980294040:AAGjViA2BCnQ9HTFMbH4ub_nD71xZ9gzlY8").build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
