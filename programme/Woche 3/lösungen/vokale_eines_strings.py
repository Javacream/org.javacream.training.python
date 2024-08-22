message = 'Hello World And MOON'
vocal_counter = 0

# Erweiterte if-Abfrage mit Collections
vocals = ('a', 'e', 'i', 'o', 'u')
for char in message:
    if char.lower() in vocals:
        vocal_counter += 1
print(vocal_counter)