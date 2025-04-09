def get_text():
    text = """
        Nimm eine Liste von Namen, filtere die Liste, das Ergebnis soll nur die Namen enthalten, die den Anfangsbuchstaben "A" haben
        """
    return text.strip()

def word_count(text):
    return len(text.split(" "))
def vowel_count(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowel_count = 0
    for character in text.lower():
        if character in vowels:
            vowel_count += 1
    return vowel_count

def main():
    text = get_text()
    number_of_words = word_count(text)
    number_of_vowels = vowel_count(text)
    print(f'{text} hat {number_of_words} Wörter und enthält {number_of_vowels} Vokale')

main()