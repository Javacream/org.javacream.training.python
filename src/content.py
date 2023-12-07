def main():
    number_of_lines = ''
    number_of_words = ''
    number_of_unique_words = ''
    number_of_unique_words_ignoring_case = ''
    def calculate_number_of_lines():
        with open('content.txt', 'r') as content_file:
            rows = content_file.readlines()
            row_count = len(rows)
            number_of_lines = f'content.txt has {row_count} rows\n'
    def calculate_number_of_words():
        with open('content.txt', 'r') as content_file:
            content = content_file.read()
            words = content.split(' ')
            word_count = len(words)
            number_of_words = f'content.txt has {word_count} words\n'
            words.sort()
            print(words)
            print([len(w) for w in words if w.startswith('b')])

    def calculate_number_of_unique():
        with open('content.txt', 'r') as content_file:
            content = content_file.read()
            words = content.split(' ')
            unique_words = set() # {} -> Fehler, das ist ein dictionary -> später
            unique_words_ignore_case = set()
            for word in words:
                unique_words.add(word)
                unique_words_ignore_case.add(word.upper())

            unique_word_count = len(unique_words)
            unique_ignore_case_word_count = len(unique_words_ignore_case)
            number_of_unique_words = f'content.txt has {unique_word_count} unique words\n'
            number_of_unique_words_ignoring_case = f'content.txt has {unique_ignore_case_word_count} unique words ignoring case\n'
    def write_to_file():        
        with open('result.txt', 'w') as outfile:
            outfile.writelines([number_of_lines, number_of_words, number_of_unique_words, number_of_unique_words_ignoring_case])

    calculate_number_of_lines()
    calculate_number_of_words()
    calculate_number_of_unique()
    write_to_file()
main()