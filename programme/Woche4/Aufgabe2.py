def count_words(text :str): # text ist ein str
    words = text.split(' ')
    length =len(words)
    return length
def main():
    text = "das ist ein simpler Text aus Wörtern"
    word_count = count_words(text)
    print(word_count)

main()