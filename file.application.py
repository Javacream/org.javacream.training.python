def main():
    number_of_words_template = "Number of words: {}"
    number_of_different_words_template = "Number of different words: {}, ignoring case {}"
    def print_out():
        for line in file:
            print(line)
    def number_of_lines():
        print(len(lines))
    def number_of_words():
        counter = 0
        for line in lines:
            counter += len(line.split(" "))
        print (number_of_words_template.format(counter))    
    def number_of_different_words(ignore_case):
        words_set = set()
        for line in lines:
            if ignore_case:
                    words_set.update([word.upper() for word in line.split(" ")])
            else:
                    words_set.update([word for word in line.split(" ")])
        print(number_of_different_words_template.format(len(words_set), ignore_case))


    filename = input ("Enter a file to analyse: ") or "README.md"
    with open('./' + filename) as file:
        print_out()
    with open('./' + filename) as file:
        lines = file.readlines()
        number_of_lines()
        number_of_words()
        number_of_different_words(True)
        number_of_different_words(False)


main()