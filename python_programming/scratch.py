def fn(list):
    list[0] = "Fritz"
    print(list[0])

def main():
    names = ["Hugo", "Emil"]
    fn(names)
    print(names[0]) # Was ist die Ausgabe: Hugo oder Fritz?

    names2 = names # Zuweisung einer Referenez, KEINE KOPIE EINES OBJEKTS
    names2[1] = "Edgar"
    print(names[1])
main()
