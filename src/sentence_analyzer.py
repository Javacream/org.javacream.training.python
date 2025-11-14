sentence = 'Das ist ein langer Text mit verschiedenen Wörtern'

length_of_sentence = len(sentence)
print(f'the sentence is {length_of_sentence} long')

number_of_whitespaces = sentence.count(' ')
print(f'the sentence has {length_of_sentence - number_of_whitespaces} characters')
print(f'the sentence has {len(sentence.replace(' ', ''))} characters')

number_of_as = sentence.count('a')
print(f'the sentence has {number_of_as} a characters')

vowels = ('a', 'e', 'i', 'o', 'u')
vowel_counter = 0
for character in sentence:
    if character in vowels:
        vowel_counter += 1

print(f'the sentence has {vowel_counter} vowels')

words = sentence.split(' ')
number_of_words = len(words)
print(f'the sentence has {number_of_words} words')




