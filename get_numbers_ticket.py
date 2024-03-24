import random

def get_numbers_ticket(min, max, quantity):
    win_cards_set = set()
    while len(win_cards_set) < quantity:
        win = random.randint(min, max)
        win_cards_set.add(win)
    win_cards = list(win_cards_set)
    return win_cards
try:
  min = int(input("Введите минимальное кол-во карточек в наборе: "))
  max = int(input("Введите максимальное кол-во карточек в наборе: "))
  quantity = int(input("Введите кол-во выигрышных карточек в наборе: "))
  
  if min < 1 or max > 1000 or quantity <= 0:
    raise ValueError

  winning_numbers = get_numbers_ticket(min, max, quantity)
  print(f"Выигрышные карточки: {winning_numbers}")
except ValueError:
  print ("Вы ввели неправильные данные. Попробуйте ещё раз.")

    
    
  
