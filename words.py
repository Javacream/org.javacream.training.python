words = []
exit_characters = ('x', 'q')
while True:
    new_word = input("Bitte ein Wort eingeben, 'x, q, X, Q'für Programmende: ")
    if len(new_word) == 1 and new_word.lower() in exit_characters:
        break
    words.append(new_word)
    index = 1
    for word in words:
        print(f"{index}. {word}")
        index = index + 1
    unique_words = set(words)
    print(f"Es wurden bisher {len(unique_words)} eindeutige Wörter eingegeben")    