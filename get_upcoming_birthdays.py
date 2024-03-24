from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smithx", "birthday": "1990.03.27"}
]

def get_upcoming_birthdays(users):
    days = 7
    today = datetime.today().date()
    upcoming_birthdays = []
    
    def dates_preparation(users):
        prepared_users = []
        for user in users:
            try:
                birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
                prepared_users.append({"name": user["name"], "birthday": birthday})
            except ValueError:
                print(f"Некорректная дата рождения для пользователя {user['name']}")
        return prepared_users
    
    prepared_users = dates_preparation(users)
    
    def find_next_weekday(d, weekday: int):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + timedelta(days=days_ahead)
    
    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
            congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratuladion date": congratulation_date_str})
    
    return upcoming_birthdays

print(get_upcoming_birthdays(users))
