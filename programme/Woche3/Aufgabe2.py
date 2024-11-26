text = "Das ist ein simpler Text. Auch das Folgende ist simpel"

# Idee: Nutzen der count-Methode
number_of_es = text.count('e')
number_of_as = text.count('a')

print(number_of_es)
print(number_of_as)

# Idee: Iteration mit Test auf Einzelzeichen
vowel_counter=0
for character in text:
    if character == 'e' or character == 'a':
        vowel_counter += 1

print(vowel_counter)

# Idee: if in auf ein Vokale-Set
vowel_counter=0
vowels = ('a', 'e', 'i', 'o', 'u')
for character in text:
    if character in vowels:
        vowel_counter += 1

print(vowel_counter)

# Idee: if in auf ein Vokale-Set inklusive Großbuchstaben
vowel_counter=0
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for character in text:
    if character in vowels:
        vowel_counter += 1

print(vowel_counter)


# Idee: if in auf ein Vokale-Set auf den in Kleinbuchstaben umgewandelte Text
vowel_counter=0
vowels = ('a', 'e', 'i', 'o', 'u')
for character in text.lower():
    if character in vowels:
        vowel_counter += 1

print(vowel_counter)