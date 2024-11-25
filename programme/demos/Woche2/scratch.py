user_input = input('Bitte eine Zahl eingeben: ')
try:
  number = int(user_input)
  print(f'Die doppelte Zahl ist {2 * number}')
except Exception as e:
    print(f'*** Ein Fehler ist aufgetreten: {e}')