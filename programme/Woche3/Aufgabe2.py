text = "Das ist ein simpler Text. Auch das Folgende ist simpel"

vowel_counter=0
vowels = ('a', 'e', 'i', 'o', 'u')
for character in text.lower():
    if character in vowels:
        vowel_counter += 1

print(vowel_counter)