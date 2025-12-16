from pyrogram import filters
from bot.ui.keyboards import start_buttons

def register(app):
    @app.on_message(filters.command("start"))
    async def start(_, m):
        await m.reply(
            "🌸 **Serena Exam Pulse** 🌸\n\n"
            "Your personalised government exam alert system.\n\n"
            "🎯 Only eligible exams\n"
            "🔔 Instant alerts\n"
            "🧠 Smart matching",
            reply_markup=start_buttons()
        )
