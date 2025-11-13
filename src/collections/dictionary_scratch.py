# Eine Menge von Key=Value-Paaren

german_english_dictionary = {'schlafen': 'sleep', 'essen': 'eat', 'trinken': 'drink', 'essen': 'take a bite'}
translation = german_english_dictionary['essen']
# translation = german_english_dictionary['arbeiten'] # KeyError
print(translation)
print('done')