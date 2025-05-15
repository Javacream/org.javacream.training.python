def read_file(path):
    with open ('text.txt', 'rt', encoding='utf-8') as file:
        content = file.read()
        content = content.replace('\n', '')
    return content
def count_characters(text):
    return len(text)

def count_alphanumeric_characters(text):
    character_counter = 0
    for char in text:
        if char.isalnum():
            character_counter += 1
    return character_counter

def count_words(text):
    words = text.split(' ')
    return len(words)
def count_unique_words(text):
    words = text.split(' ')
    words_without_duplicates = set(words)
    return len(words_without_duplicates)

def smallest_words(text):
    min_words = set()
    min_words_length = 9999999
    words = text.split(' ')

    for word in words:
        if len(word) < min_words_length:
            min_words_length = len(word)

    for word in words:
        if len(word) == min_words_length:
            min_words.add(word)
    return (min_words_length, min_words)

def lengthiest_words(text):
    max_words = set()
    max_words_length = 0
    words = text.split(' ')
    for word in words:
        if len(word) > max_words_length:
            max_words_length = len(word)

    for word in words:
        if len(word) == max_words_length:
            max_words.add(word)
    return (max_words_length, max_words)

def write_result(result_dictionary):
    print(result_dictionary)

def create_result(character_count, alphanumeric_character_count, word_count, unique_word_count, smallest, lengthiest):
    result = dict()
    result['character_count'] = character_count
    result['alphanumeric_character_count'] = alphanumeric_character_count
    result['word_count'] = word_count
    result['unique_character_count'] = unique_word_count
    result['smallest'] = smallest
    result['lengthiest'] = lengthiest

def main():
    file_path = 'text.txt'
    content = read_file(file_path)
    character_count = count_characters(content)
    alphanumeric_character_count = count_alphanumeric_characters(content)
    word_count = count_words(content)
    unique_word_count = count_unique_words(content)
    smallest = smallest_words(content)
    lengthiest = lengthiest_words(content)
    result = create_result(character_count, alphanumeric_character_count, word_count, unique_word_count, smallest, lengthiest)
    write_result(result)
main()