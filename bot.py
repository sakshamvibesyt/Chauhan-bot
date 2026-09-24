import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


# =========================================================
# BOT TOKEN
# Render → Environment → BOT_TOKEN mein token add karo.
# =========================================================
BOT_TOKEN = os.getenv("BOT_TOKEN")


# =========================================================
# CHANNELS
#
# YAHAN APNE CHANNELS KI LINKS DALO.
#
# Example:
# "🔥 𝐉𝐀𝐋𝐁𝐀": "https://t.me/yourchannel"
#
# Jitne channels chaho utne add kar sakte ho.
# =========================================================

CHANNELS = {
    "🔥 𝐉𝐀𝐋𝐁𝐀": "https://t.me/+ncQKOjYSU3o5MGZl",
    "💀 𝗧𝗥𝗫": "https://t.me/+R--o4zJimuxhNDM1",
    "📢 𝗧𝗥𝗫 II": "https://t.me/+oiU1AGIiPWQ0NzU1",
    "🎮 𝗚𝗿𝗼𝘂𝗽": "https://t.me/+LZX1DMqIaUs0Mjc1",
}


# =========================================================
# DEVELOPER
# =========================================================

DEVELOPER_NAME = "⚡ ⲟⲱⲛⲉⲅ"
DEVELOPER_LINK = "https://t.me/MR3CHOUHAN4"


# =========================================================
# RENDER WEB SERVER
# =========================================================

web = Flask(__name__)


@web.route("/")
def home():
    return "Chouhan XD Bot is running! ✅", 200


@web.route("/health")
def health():
    return "OK", 200


def run_web_server():
    port = int(os.environ.get("PORT", 10000))

    web.run(
        host="0.0.0.0",
        port=port,
        use_reloader=False
    )


# =========================================================
# /START COMMAND
# =========================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    # User name
    name = user.full_name or "User"

    # Username
    if user.username:
        username = f"@{user.username}"
    else:
        username = "Username not set"

    # =====================================================
    # WELCOME MESSAGE
    # =====================================================

    text = (
        "╭━━━━━━━━━━━━━━━━━━━━╮\n"
        "       ✦ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 ✦\n"
        "╰━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"👤 𝐍𝐚𝐦𝐞 : {name}\n"
        f"🔗 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : {username}\n\n"

        "✨ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐂𝐡𝐨𝐮𝐡𝐚𝐧 𝐗𝐃 𝐁𝐨𝐭!\n\n"

        "📢 𝐂𝐡𝐞𝐜𝐤 𝐨𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬 👇\n\n"

        "⚡ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐛𝐲 @Sakshamvenus"
    )


    # =====================================================
    # CHANNEL BUTTONS
    # =====================================================

    buttons = []

    for channel_name, channel_link in CHANNELS.items():

        buttons.append(
            InlineKeyboardButton(
                text=channel_name,
                url=channel_link
            )
        )


    # 2 buttons per row
    keyboard = []

    for i in range(0, len(buttons), 2):

        row = buttons[i:i + 2]

        keyboard.append(row)


    # =====================================================
    # DEVELOPER BUTTON
    # =====================================================

    keyboard.append(
        [
            InlineKeyboardButton(
                text=DEVELOPER_NAME,
                url=DEVELOPER_LINK
            )
        ]
    )


    reply_markup = InlineKeyboardMarkup(keyboard)


    # =====================================================
    # SEND MESSAGE
    # =====================================================

    await update.message.reply_text(
        text=text,
        reply_markup=reply_markup
    )


# =========================================================
# MAIN
# =========================================================

def main():

    # Token check
    if not BOT_TOKEN:

        raise ValueError(
            "BOT_TOKEN nahi mila! "
            "Render → Environment mein BOT_TOKEN add karo."
        )


    # Render ke liye web server start
    web_thread = threading.Thread(
        target=run_web_server,
        daemon=True
    )

    web_thread.start()


    # Telegram application
    application = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )


    # /start handler
    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    print("=================================")
    print("     CHOUHAN XD BOT STARTED")
    print("=================================")
    print("Telegram bot is running...")


    # Telegram polling
    application.run_polling(
        drop_pending_updates=True
    )


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":
    main()
