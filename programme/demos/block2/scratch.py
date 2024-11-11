user_input = 'Hugo'

try:
  number = int(user_input)
  # e r r o r SyntxErrors können nie behandelt werden
  print(2 * number)
except Exception as e: # Dieses "Exception as e" bitte akzeptieren
    print(f'*** Ein Fehler ist aufgetreten: {e}')
    # print(f'{user_input} kann nicht in eine Zahl konvertiert werden')

print('nächste Programmanweisung')    