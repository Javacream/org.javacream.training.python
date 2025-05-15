def read_file(path):
    pass
    return ''

def count_characters(text):
    pass
    return 0

def count_alphanumeric_characters(text):
    pass
    return 0

def count_words(text):
    pass
    return 0

def count_unique_words(text):
    pass
    return 0

def smallest_words(text):
    pass
    return (0, [])

def lengthiest_words(text):
    pass
    return (0, [])

def write_result(result_dictionary):
    pass

def main():
    file_path = 'text.txt'
    content = read_file(file_path)
    character_count = count_characters(content)
    alphanumeric_character_count = count_alphanumeric_characters(content)
    word_count = count_words(content)
    unique_word_count = count_unique_words(content)
    smallest = smallest_words(content)
    lengthiest = lengthiest_words(content)
    result = dict()
    result['character_count'] = character_count
    result['alphanumeric_character_count'] = alphanumeric_character_count
    result['word_count'] = word_count
    result['unique_character_count'] = unique_word_count
    result['smallest'] = smallest
    result['lengthiest'] = lengthiest
    write_result(result)
main()