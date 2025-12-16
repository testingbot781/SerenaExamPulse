from .age_calc import calculate_age
import json

def check_user_eligibility(user, exam):
    qualifications = json.loads(user[6])
    age = calculate_age(user[3])

    if age < exam["age_min"] or age > exam["age_max"]:
        return False

    if not any(q in exam["qualification"] for q in qualifications):
        return False

    if user[2] not in exam["states"] and "ALL" not in exam["states"]:
        return False

    return True
