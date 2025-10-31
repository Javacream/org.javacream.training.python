def words(text):
    words = text.split(' ')
    return words

def words_length(words):
    return len(words)

def main():
    sentence = 'a very simple demo text with a number of words'
    words_of_sentence = words(sentence)
    length = words_length(words_of_sentence)
    print(length) 
main()