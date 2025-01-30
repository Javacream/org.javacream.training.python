def words_of_text(text :str):
    return text.split(" ")

if __name__ == '__main__':
    demo_text = "Im Wald da sind die Räuber"
    numbers_of_words = len(words_of_text(demo_text))
    print(f'Die Anzahl der Wörter ist {numbers_of_words}')