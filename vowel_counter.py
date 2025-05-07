vowels = ('a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü')
text = input ('Bitte einen beliebigen Text eingeben: ')
text_lower_case = text.lower()
vowel_counter = 0
for vowel in vowels:
    vowel_counter += text_lower_case.count(vowel)

print(f"Der eingegebene Text {text} enthält {vowel_counter} Vokale")        
