from datetime import datetime

def get_days_from_today(date_str: str) -> int:
  try:
    now_date = datetime.today().date()
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    delta = now_date - date_obj
    return delta.days
  except ValueError:
      print("Некорректный формат даты. Попробуйте ещё раз :)")
      date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
      return get_days_from_today(date_str)
    
  

date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
print(get_days_from_today(date_str))
