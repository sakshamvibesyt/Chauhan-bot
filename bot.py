import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "PASTE_YOUR_BOT_TOKEN_HERE")

CHANNELS = {
    "🔥 𝐉𝐀𝐋𝐁𝐀": "https://t.me/YOUR_JALBA_CHANNEL",
    "💀 𝐃𝐃𝐎𝐒": "https://t.me/YOUR_DDOS_CHANNEL",
    "📢 𝐌𝐀𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋": "https://t.me/YOUR_MAIN_CHANNEL",
    "🎮 𝐆𝐀𝐌𝐈𝐍𝐆": "https://t.me/YOUR_GAMING_CHANNEL",
}

DEVELOPER_NAME = "⚡ 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑"
DEVELOPER_LINK = "https://t.me/Sakshamvenus"

web = Flask(__name__)

@web.get("/")
def home():
    return "Chouhan XD Bot is running!", 200

@web.get("/health")
def health():
    return "OK", 200

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port, use_reloader=False)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else "Username not set"
    name = user.full_name or "User"

    text = (
        "╭━━━━━━━━━━━━━━━━━━╮\n"
        "      ✦ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 ✦\n"
        "╰━━━━━━━━━━━━━━━━━━╯\n\n"
        f"👤 𝐍𝐚𝐦𝐞 : {name}\n"
        f"🔗 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : {username}\n\n"
        "✨ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐦𝐲 𝐁𝐨𝐭!\n"
        "📢 𝐂𝐡𝐞𝐜𝐤 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐛𝐞𝐥𝐨𝐰 👇\n\n"
        "⚡ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐰𝐢𝐭𝐡 𝐋𝐨𝐯𝐞 𝐛𝐲 𝐒𝐚𝐤𝐬𝐡𝐚𝐦"
    )

    buttons = [InlineKeyboardButton(label, url=link) for label, link in CHANNELS.items()]
    keyboard = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    keyboard.append([InlineKeyboardButton(DEVELOPER_NAME, url=DEVELOPER_LINK)])

    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    if BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        raise ValueError("BOT_TOKEN Render Environment mein add karo.")

    threading.Thread(target=run_web, daemon=True).start()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
