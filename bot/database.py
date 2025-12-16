from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["serena_exam_pulse"]

users = db["users"]       # user profiles
blocked = db["blocked"]   # block tracking
exams = db["exams"]       # admin exam postings
