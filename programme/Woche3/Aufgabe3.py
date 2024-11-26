text = "Das ist ein simpler Text. Auch das Folgende ist simpel"

words_list = text.split(' ')
#print(words_list)
#words_list_as_text = str(words_list)
#print(words_list_as_text)

# words_list_as_text = ''
# for word in words_list:
#     words_list_as_text = f'{words_list_as_text} {word}'
# print(words_list_as_text)

print(' '.join(words_list))
