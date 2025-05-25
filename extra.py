from datetime import date

def calculate_age(birth_date_str):
    birth_date = date.fromisoformat(birth_date_str)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age