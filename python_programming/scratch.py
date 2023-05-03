def listDemo():
    names = ["A", "B", "A", "C"]
    print(names[1]) # -> B
    print(len(names))
    names.append("X")
    names.append("A")
    print(len(names))
    for name in names:
        print(name)

def setDemo():
    names = {"A", "B", "A", "C"}
    #print(names[1]) # -> B
    print(len(names))
    names.add("X")
    names.add("A")
    print(len(names))
    for name in names:
        print(name)


def tupleDemo():
    namesList = ["A", "B", "A"]
    namesList[1] = "C"
    namesTuple = ("A", "B", "A")
    #namesTuple[1] = "C"
    print(namesTuple[1])
    for name in namesTuple:
        print(name)

def rangeDemo():
    r = range (1, 9, 2)
    for n in r:
        print(n)

def dictionaryDemo():
    postalCodesLookup = {81371: "München", 30001: "Belin", 40022: "Hamburg"}
    print(postalCodesLookup[81371])
    #print(postalCodesLookup[81372]) #Laufzeitfehler bei nicht vorhandenem Key -> später finden wir eine bessere Lösung
    for key in postalCodesLookup.keys():
        print(f"Key: {key}")
    for value in postalCodesLookup.values():
        print(f"Value: {value}")
    for key, value in postalCodesLookup.items():
        print(f"Key: {key}, Value: {value}")
def main():
    dictionaryDemo()
main()