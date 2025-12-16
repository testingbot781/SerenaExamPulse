import asyncio
from threading import Thread
from flask import Flask
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import start, help, settings, profile, admin
from bot.scheduler import init_scheduler


# -----------------------------
# Flask server for Render
# -----------------------------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Serena Exam Pulse is running!"

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


async def main_bot():
    await app.start()
    print("Bot started successfully ✔")

    init_scheduler(app)
    print("Scheduler started ✔")

    # Keep bot alive forever (no stop, no idle)
    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    # Run Flask in background thread
    Thread(target=run_flask, daemon=True).start()

    # Run bot in main thread / main loop
    asyncio.run(main_bot())

