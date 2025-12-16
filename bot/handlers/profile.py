from pyrogram import filters
from bot.database import users
import json

def register(app):

    @app.on_message(filters.command("profile"))
    async def ask_profile(_, m):
        await m.reply(
            "👤 **Profile Setup**\n\n"
            "Send your details in this format:\n"
            "`State, DOB(YYYY-MM-DD), Gender, Category`\n"
            "Example:\n"
            "`Bihar, 2002-06-11, Female, OBC`"
        )

    @app.on_message(filters.text & ~filters.command("profile"))
    async def save_profile(_, m):
        try:
            state, dob, gender, category = [i.strip() for i in m.text.split(",")]

            users.update_one(
                {"user_id": m.from_user.id},
                {
                    "$set": {
                        "user_id": m.from_user.id,
                        "name": m.from_user.first_name,
                        "state": state,
                        "dob": dob,
                        "gender": gender,
                        "category": category,
                        "qualifications": [],
                        "preferences": []
                    }
                },
                upsert=True
            )

            await m.reply(
                "✅ **Profile Saved Successfully!**\n"
                "अब आप /settings या qualification add कर सकते हैं।"
            )

        except:
            await m.reply("❌ Invalid Format! Example देखो:\n`Bihar, 2002-06-11, Female, OBC`")
