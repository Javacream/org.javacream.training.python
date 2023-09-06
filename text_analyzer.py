def count_all_words(text):
    return len(text.split(" "))

def count_all_unique_words(text):
    all_words = text.split(" ")
    unique_words = set()
    for word in all_words:
        unique_words.add(word)
    return len(unique_words)

def count_all_unique_words_ignore_case(text):
    all_words = text.split(" ")
    unique_words = set()
    for word in all_words:
        unique_words.add(word.lower())
    return len(unique_words)

def main():
    textfile = open('text.txt', 'r')
    text = textfile.read()

    print(count_all_words(text))
    print(count_all_unique_words(text))
    print(count_all_unique_words_ignore_case(text))    

main()