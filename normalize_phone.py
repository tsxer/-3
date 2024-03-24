import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone (phone_number):
  pattern = r"\D"
  phone_number_clear = re.sub(pattern, "",  phone_number)
  if phone_number_clear.startswith("+380"):
    pass
  elif phone_number_clear.startswith("380"):
    phone_number_clear = "+" + phone_number_clear
  elif phone_number_clear.startswith ("0"):
    phone_number_clear = "+38" + phone_number_clear
  else:
    phone_number_clear = "+380" + phone_number_clear
  return phone_number_clear
    

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормализованные номера телефонов для SMS-рассылки: ", sanitized_numbers)
