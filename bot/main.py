from threading import Thread
import asyncio
from flask import Flask
from pyrogram import Client, idle
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import start, help, settings, profile, admin
from bot.scheduler import init_scheduler


# -----------------------------
# Flask server
# -----------------------------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Serena Exam Pulse bot is running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)


# -----------------------------
# Pyrogram Bot
# -----------------------------
app = Client(
    "SerenaExamPulse",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

start.register(app)
help.register(app)
settings.register(app)
profile.register(app)
admin.register(app)


async def start_bot():
    await app.start()
    print("🔥 Bot started successfully!")

    init_scheduler(app)
    print("⏳ Scheduler started!")

    await idle()  # Pyrogram का built‑in stable loop


def run_bot():
    asyncio.run(start_bot())


# -----------------------------
# Start Both Services
# -----------------------------
if __name__ == "__main__":
    # Run Flask (Render wants open port)
    Thread(target=run_flask, daemon=True).start()

    # Run Telegram Bot in background
    Thread(target=run_bot, daemon=True).start()

    # Keep main thread alive
    while True:
        pass

