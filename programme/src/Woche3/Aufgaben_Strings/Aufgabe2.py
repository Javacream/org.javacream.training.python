text = "Schreiben Sie Ein Python-Programm, das alle Vokale in einem gegebenen String zählt, AUCH GROSSBUCHSTABEN"

vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')

vowel_counter = 0
for character in text:
    if character in vowels:
        vowel_counter += 1
print(vowel_counter)
