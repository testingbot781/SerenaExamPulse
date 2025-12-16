# 🌸 Serena Exam Pulse

A smart Telegram bot that sends government exam alerts based on the user's profile and eligibility.

## Features
- Eligibility-based exam filtering
- Inline Apply Now buttons
- Multi-degree support
- Admin dashboard (/status /users)
- Aesthetic UI

## Deployment
1. Upload code to GitHub
2. Create a Web Service on Render
3. Add env variables:
   BOT_TOKEN=
   API_ID=
   API_HASH=
   ADMIN_ID=
4. Start command:
   python -m bot.main


# Serena Exam Pulse 🌸

A Telegram bot that notifies users about government exams
based on eligibility (age, qualification, state, category).

## Features
- Personalized eligibility alerts
- Inline apply buttons
- User profile & settings panel
- Admin monitoring commands

## Deploy on Render
Start Command:
python -m bot.main


🚀 RENDER SETTINGS
Service Type: Web Service

Build: pip install -r requirements.txt

Start: python -m bot.main

ENV: BOT_TOKEN=xxxx
