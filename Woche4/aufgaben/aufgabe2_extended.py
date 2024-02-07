def main():
    def word_count(text):
        words_list = text.split(" ")
        return len(words_list)
    
    text = "This is a text with some demo content and data"
    print(word_count(text))

    def word_count_with_options(text, **kwargs):
        words_list = text.split(" ")
        starts_with = kwargs.get('startswith')
        matching_words = []
        if starts_with:
            for word in words_list:
                if word.startswith(starts_with):
                    matching_words.append(word)
        else:
            matching_words = words_list
        return len(matching_words)

    print(word_count_with_options(text))
    print(word_count_with_options(text, startswith = 'd'))
    print(word_count_with_options(text, startswith = 'w'))

main()