with open ('./programme/demos/block3/text.txt', 'rt') as file:
    rows = file.readlines()
    text = ''
    for row in rows:
        if row[-1] == '\n':
            text += row[:-1]
        else:
            text += row
characters_to_count = input ('Bitte die zu zählenden Zeichen kommasepariert eingeben:')
characters_to_count = characters_to_count.split(',')

result = []

for character in characters_to_count:
    result.append([character, 0])

character_count = 0
for character in text:
    if character in characters_to_count:
        for character_count_for_character in result:
            if character == character_count_for_character[0]:
                character_count_for_character[1] += 1
            continue    

print(result)