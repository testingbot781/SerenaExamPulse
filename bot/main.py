from threading import Thread
import asyncio
from flask import Flask
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import start, help, settings, profile, admin
from bot.scheduler import init_scheduler


# -----------------------------------
# Flask server (Render requirement)
# -----------------------------------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Serena Exam Pulse bot is running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)


# -----------------------------------
# Telegram Bot (Pyrogram)
# -----------------------------------
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


async def bot_loop():
    await app.start()
    print("🔥 Bot started successfully!")
    init_scheduler(app)
    print("⏳ Scheduler started!")

    # Keep bot alive forever WITHOUT idle(), WITHOUT signals
    while True:
        await asyncio.sleep(3)


def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot_loop())


# -----------------------------------
# Start Both Services
# -----------------------------------
if __name__ == "__main__":
    Thread(target=run_flask, daemon=True).start()
    Thread(target=run_bot, daemon=True).start()

    # Prevent main thread from exiting
    while True:
        pass

