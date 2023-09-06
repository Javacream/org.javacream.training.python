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

def analyse(text):
    print(count_all_words(text))
    print(count_all_unique_words(text))
    print(count_all_unique_words_ignore_case(text))    

def main():
    while(True):
        filename = input("please enter a file to analyze, exit or x to stop: ")
        if (filename in ('', 'exit', 'x')):
            break
        try:
            textfile = open(filename, 'r')
            text = textfile.read()
            analyse(text)
        except:
            print("file not found: " + filename)

main()