def count_words(text :str): # text ist ein str
    words = text.split(' ')
    length =len(words)
    return length
def test():
    text = "das ist ein simpler Text aus Wörtern"
    word_count = count_words(text)
    print(word_count)

if __name__ == '__main__':
    test()