text = "Schreiben Sie Ein Python-Programm, das alle Vokale in einem gegebenen String zählt, AUCH GROSSBUCHSTABEN"

vowel_counter = 0

for character in text:
    if character == 'e':
        vowel_counter +=1
    elif character == 'E':
        vowel_counter +=1
    elif character == 'A':
        vowel_counter +=1
    elif character == 'I':
        vowel_counter +=1
    elif character == 'O':
        vowel_counter +=1
    elif character == 'U':
        vowel_counter +=1
    elif character == 'a':
        vowel_counter +=1
    elif character == 'i':
        vowel_counter +=1
    elif character == 'u':
        vowel_counter +=1
    elif character == 'o':
        vowel_counter +=1

print(vowel_counter)

vowel_counter = 0
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 
for character in text:
    if character in vowels:
        vowel_counter += 1

print(vowel_counter)

vowel_counter = 0
vowels = {'a', 'e', 'i', 'o', 'u'} 
for character in text:
    if character.lower() in vowels:
        vowel_counter += 1

print(vowel_counter)
