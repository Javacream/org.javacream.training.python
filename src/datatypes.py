def main():
    a = "Hu"
    b = "Go"
    c = "4"
    d = "2"
    e = 4
    f = 2
    g = 1.1
    h = 4.4

    result = a + b
    result = e + f
    result = c + d

    # Die folgenden Anweisungen sind nun aber kritisch
    # result = e + a # TypeError
    # result = a + 4 # TypeError

    #Typumwandlung durch build-in functions str(), int(), float()
    c_as_int = int(c) # Typumwandlung, exakt: ein neues Objekt wird erzeugt
    e_as_str = str(e)
    result = c_as_int + e
    result = a + e_as_str

    result = e + g # das geht, obwohl im strengen Sinn die Tpen nicht passen

    # Details
    result = float(e) + g

    result = e + int(g)
    print(result, type(result))
main()