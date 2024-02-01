def reverse_string(original_string):
    #reversed_string = original_string[1:3] # 1:3 -> "von bis", "Slicing"
    #reversed_string = original_string[:3] # -> "von bis", start implizit 0"
    #reversed_string = original_string[1:] # 1: -> "von bis", Ende ist implizit die Länge des Strings -1
    reversed_string = original_string[::-1] # -1: Slicing von oben nach unten
    print(reversed_string)

def count_vocals(text):
    vocals = ("a", "e", "i", "o", "u")
    counter = 0
    for character in text:
        if  character.lower() in vocals:
            counter +=1
    print(f"Die Zeichenkette {text} enthält {counter} Vokale")

def string_to_list_and_back():
    text = """Schreiben Sie ein Python-Programm, das einen String in eine Liste von Wörtern
umwandelt, und dann die Liste wieder in einen String umwandelt."""
    words = text.split(" ")
    print(words)
    sentence = " ".join(words)
    print(sentence)

def main():
    string_input = input("Bitte geben Sie einen Text ein: ")
    #reverse_string(string_input)
    #count_vocals(string_input)
    string_to_list_and_back()

main()