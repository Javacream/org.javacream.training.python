import text_analysis as ta
def main():
    file_path = 'text.txt'
    content = ta.read_file(file_path)
    character_count = ta.count_characters(content)
    alphanumeric_character_count = ta.count_alphanumeric_characters(content)
    word_count = ta.count_words(content)
    unique_word_count = ta.count_unique_words(content)
    smallest = ta.smallest_words(content)
    lengthiest = ta.lengthiest_words(content)
    result = ta.create_result(character_count, alphanumeric_character_count, word_count, unique_word_count, smallest, lengthiest)
    ta.write_result(result)

main()
