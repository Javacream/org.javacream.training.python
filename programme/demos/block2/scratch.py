user_input = 'Hugo'

try:
  number = int(user_input)
  print(2 * number)
except:
    print(f'{user_input} kann nicht in eine Zahl konvertiert werden')

print('nächste Programmanweisung')    