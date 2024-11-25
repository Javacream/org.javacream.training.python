text = 'Also das ist ein einfacher Text ohne Kommas oder Punkte oder Ausrufezeichen damit ist das Kriterium für Wörter das Leerzeichen'
text = text.lower()
vowels = ('a', 'e', 'i', 'o', 'u')

vocal_count = 0

for character in text:
    if character in vowels:
        vocal_count += 1

print(vocal_count)