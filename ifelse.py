def main():
    a  = 5
    b = 38
    condition = a < b
    if condition:
        print("a < b")
    
    if a < b:
        print("a < b")

    if a == 5:
        pass # leere Anwesiung, damit die Syntax mit Einrückung stimmt
    elif a == 42:
        pass
    elif a == 3:
        pass
    else:
        pass


    # verschachtelte ifs
    if a == 5:
        if b == 32:
            pass
        elif b == 55:
            pass
        else:
            pass
    else:
        pass


    # Verkürzungen (optional)

    if a < b:
        print("a < b")
    else:
        print("a >= b")

    print("a < b") if a < b else print("a >= b")    

    if a < b: print("a < b")


main()