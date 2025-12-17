from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.logic.eligibility import check_user_eligibility
from bot.database import users
from bot.ui.keyboards import exam_apply_button
import json

scheduler = AsyncIOScheduler()

def init_scheduler(app):
    @scheduler.scheduled_job("interval", hours=1)
    async def send_alerts():
        exams = json.load(open("bot/data/exams.json"))
        all_users = list(users.find({}))

        for user in all_users:
            user_id = user["user_id"]

            for exam in exams:
                if check_user_eligibility(user, exam):
                    await app.send_message(
                        user_id,
                        f"📢 **New Exam Opportunity!**\n\n"
                        f"📝 **Exam:** {exam['name']}\n"
                        f"💰 **Salary:** {exam['salary']}\n"
                        f"🎓 **Qualification:** {', '.join(exam['qualification'])}\n"
                        f"🎂 **Age Limit:** {exam['age_min']}–{exam['age_max']}\n"
                        f"📍 **States:** {', '.join(exam['states'])}\n\n"
                        "👇 Apply below",
                        reply_markup=exam_apply_button(exam["apply_link"])
                    )

    scheduler.start()
    
