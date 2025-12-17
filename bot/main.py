import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import start, help, settings, profile, admin
from bot.scheduler import init_scheduler


app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return "Serena Exam Pulse bot is running (Stable Render Mode)"


# -----------------------------
# Pyrogram bot (same process)
# -----------------------------
pyro_app = Client(
    "SerenaExamPulse",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

start.register(pyro_app)
help.register(pyro_app)
settings.register(pyro_app)
profile.register(pyro_app)
admin.register(pyro_app)


async def start_bot():
    print(">>> Starting bot...")
    await pyro_app.start()
    print("🔥 Bot started successfully!")
    init_scheduler(pyro_app)
    print("⏳ Scheduler started!")

    # keep bot alive
    while True:
        await asyncio.sleep(5)


def run_asyncio_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # BOT RUNS INSIDE SAME PROCESS (NO THREAD CRASH)
    loop.create_task(start_bot())

    loop.run_forever()


# -----------------------------
# Start both
# -----------------------------
if __name__ == "__main__":
    # Flask separate thread (Render requirement)
    Thread(target=lambda: app_flask.run(host="0.0.0.0", port=10000), daemon=True).start()

    # Run asyncio bot in main thread
    run_asyncio_loop()

