filename = './Tag2/demo.txt'
with open(filename) as file:
    rows = file.readlines()
    print(f"{filename} has {len(rows)} rows")
    words = []
    for row in rows:
        words = words + row.split() # Jawohl, wir können Listen einfach addieren!
    print(f"{filename} has {len(words)} words")
    unique_words = set(words)
    print(f"{filename} has {len(unique_words)} unique words")
    max_word_length = 0
    min_word_length = 999
    for word in words:
        word_length = len(word)
        if len(word) > max_word_length:
            max_word_length = word_length
        if len(word) < min_word_length:
            min_word_length = word_length
    max_length_words = set()
    min_length_words = set()
    for word in words:
        if len(word) == max_word_length:
            max_length_words.add(word)
        if len(word) == min_word_length:
            min_length_words.add(word)
    print(f"Longest words in {filename} are {max_length_words}")
    print(f"Shortest words in {filename} are {min_length_words}")

