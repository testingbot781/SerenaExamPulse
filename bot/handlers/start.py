from pyrogram import filters
from bot.ui.keyboards import start_buttons

def register(app):
    @app.on_message(filters.command("start"))
    async def start(_, m):
        await m.reply(
            "🌸 **Serena Exam Pulse** 🌸\n\n"
            "Smart Government Exam Alerts Based On Your Eligibility.\n\n"
            "🎯 Accurate Match\n"
            "🔔 Instant Notifications\n"
            "🧠 Smart Profile Engine\n\n"
            "👇 Start below",
            reply_markup=start_buttons()
        )
