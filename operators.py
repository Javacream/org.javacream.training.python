def main():
    name = "Hugo"
    # skurril
    result = 4 * name
    print(result)
    # result = name / 2 # geht nicht

    # LOGISCHE OPERATOREN
    state1 = True
    state2 = False

    print(type(state1))
    # bitte nicht:
    result = state1 + state2
    print(result, type(result))

    # statt dessen: Logische Operatoren
    result = not state1
    print(result, type(result))

    result = state1 and state2
    print(result, type(result))

    result = state1 or state2
    print(result, type(result))

    # VERGLEICHSOPERATOREN

    number1 = 42
    number2 = 1
    print(number1 == number2)
    print(number1 != number2)
    print(number2 == True) # in Python, Sawitzki findet das aber blöde
    print(number1 <= number2)
    print(number1 >= number2)



main()