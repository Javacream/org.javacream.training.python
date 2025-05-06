vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
text = input ('Bitte einen beliebigen Text eingeben: ')
vowel_counter = 0
for character in text:
    if character in vowels:
        vowel_counter += 1
print(f"Der eingegebene Text {text} enthält {vowel_counter} Vokale")        
