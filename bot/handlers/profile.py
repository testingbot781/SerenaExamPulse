from pyrogram import filters
from bot.database import db, conn
import json

def register(app):
    @app.on_message(filters.command("profile"))
    async def profile(_, m):
        await m.reply(
            "👤 **Profile Setup**\n\n"
            "Send your details in this format:\n"
            "`State, DOB(YYYY-MM-DD), Gender, Category`\n"
            "Example:\n"
            "`Bihar, 2002-06-11, Female, OBC`"
        )
