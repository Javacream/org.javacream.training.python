words = []
while True:
    new_word = input("Bitte ein Wort eingeben, 'x' für Programmende: ")
    if 'x' == new_word:
        break
    words.append(new_word)
    index = 1
    for word in words:
        print(f"{index}. {word}")
        index = index + 1
    unique_words = set(words)
    print(f"Es wurden bisher {len(unique_words)} eindeutige Wörter eingegeben")    