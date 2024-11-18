with open ('./programme/demos/block3/text.txt', 'rt') as file:
    rows = file.readlines()
    text = ''
    for row in rows:
        if row[-1] == '\n':
            text += row[:-1]
        else:
            text += row
characters_to_count = input ('Bitte die zu zählenden Zeichen kommasepariert eingebn:')
characters_to_count = characters_to_count.split(',')

character_count = 0
for character in text:
    if character in characters_to_count:
        character_count += 1

print(character_count)