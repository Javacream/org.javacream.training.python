with open ('text.txt', 'rt', encoding='utf-8') as file:
    content = file.read()
    content = content.replace('\n', '')

print(f"Der gelesene Text besteht aus {len(content)} Zeichen")

character_counter = 0
for char in content:
    if char.isalnum():
        character_counter += 1
print(f"Der gelesene Text besteht aus {character_counter} alphanumerischen Zeichen")

words = content.split(' ')
print(f"Der gelesene Text besteht aus {len(words)} Wörtern")
words_without_duplicates = set(words)
print(f"Der gelesene Text besteht aus {len(words_without_duplicates)} unterschiedlichen Wörtern")

max_words = set()
min_words = set()
min_words_length = 9999999
max_words_length = 0
for word in words:
    if len(word) < min_words_length:
        min_words_length = len(word)
    if len(word) > max_words_length:
        max_words_length = len(word)

for word in words:
    if len(word) == max_words_length:
        max_words.add(word)
    if len(word) == min_words_length:
        min_words.add(word)

print(f'Die längsten Wörter sind {max_words} mit einer Länge von {max_words_length}')
print(f'Die kürzesten Wörter sind {min_words} mit einer Länge von {min_words_length}')

