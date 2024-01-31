def reverse_string(original_string):
    #reversed_string = original_string[1:3] # 1:3 -> "von bis", "Slicing"
    #reversed_string = original_string[:3] # -> "von bis", start implizit 0"
    #reversed_string = original_string[1:] # 1: -> "von bis", Ende ist implizit die Länge des Strings -1
    reversed_string = original_string[::-1] # -1: Slicing von oben nach unten
    print(reversed_string)

def count_vocals_verbose(text):
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    counter = 0
    for character in text:
        if character == a:
            counter +=1
        elif character == e:
            counter +=1
        elif character == i:
            counter +=1
        elif character == o:
            counter +=1
        elif character == u:
            counter +=1
    print(f"Die Zeichenkette {text} enthält {counter} Vokale")

def count_vocals(text):
    vocals = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    counter = 0
    for character in text:
        if character in vocals:
            counter +=1
    print(f"Die Zeichenkette {text} enthält {counter} Vokale")
def main():
    string_input = input("Bitte geben Sie einen Text ein: ")
    #reverse_string(string_input)
    count_vocals(string_input)

main()