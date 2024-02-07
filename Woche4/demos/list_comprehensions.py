def main():
    text = "This is a text with some demo content and data"
    words_list = text.split(" ")
    words_starting_with_d = [word for word in words_list if word.startswith('d')]
    print(words_starting_with_d)
    capitalized_words_starting_with_d = [word.upper() for word in words_list if word.startswith('d')]
    print(capitalized_words_starting_with_d)
    x = [len(word) for word in words_list]
    print(x)

main()