from pyrogram import filters

def register(app):
    @app.on_message(filters.command("help"))
    async def help(_, m):
        await m.reply(
            "📘 **Help Panel**\n\n"
            "/profile – Set your details\n"
            "/settings – Customize notifications\n"
            "/preferences – Select exam categories\n"
            "/start – Restart bot UI"
        )
