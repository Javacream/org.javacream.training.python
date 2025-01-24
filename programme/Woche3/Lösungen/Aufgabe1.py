name = "Hugo"
reversed_name = name[::-1]
print(reversed_name)
text = "Schreiben Sie Ein Python-Programm, das alle Vokale in einem gegebenen String zählt."

number_of_es = text.count('e')
print(number_of_es)

number_of_is = text.count('i')
print(number_of_is),

#...

vowels = ('a', 'e', 'i', 'o', 'u')

vowel_counter = 0
for character in text.lower():
    if character in vowels:
        vowel_counter += 1
print(vowel_counter)

words = text.split(' ')
print(words)
print(" ".join(words))

