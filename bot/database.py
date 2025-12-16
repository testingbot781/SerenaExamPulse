import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
db = conn.cursor()

db.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    state TEXT,
    dob TEXT,
    gender TEXT,
    category TEXT,
    qualifications TEXT,
    preferences TEXT
)
""")

db.execute("""
CREATE TABLE IF NOT EXISTS blocked (
    user_id INTEGER PRIMARY KEY
)
""")

conn.commit()
