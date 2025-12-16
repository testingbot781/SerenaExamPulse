from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.database import db, conn
import json
from bot.logic.eligibility import check_user_eligibility

scheduler = AsyncIOScheduler()

def start_scheduler(app):
    @scheduler.scheduled_job("interval", minutes=60)
    async def send_alerts():
        exams = json.load(open("bot/data/exams.json"))
        db_users = db.execute("SELECT * FROM users").fetchall()

        for user in db_users:
            user_id = user[0]
            for exam in exams:
                if check_user_eligibility(user, exam):
                    await app.send_message(
                        user_id,
                        f"📢 New Exam Alert!\n\n"
                        f"📝 {exam['name']}\n"
                        f"💰 Salary: {exam['salary']}\n"
                        f"🎓 Qualification: {exam['qualification']}\n"
                        f"🎂 Age Limit: {exam['age_min']} - {exam['age_max']}\n\n"
                        "👇 Apply below",
                        reply_markup=exam_apply_button(exam["apply_link"])
                    )

    scheduler.start()
