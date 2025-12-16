from datetime import datetime

def calculate_age(dob):
    dob = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
