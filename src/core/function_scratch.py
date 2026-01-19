def add(number1, number2):
    result = number1 + number2
    return result

def main():
    n1 = 22
    n2 = 20
    add_result = add(n1, n2) # implizit im Aufruf: number1 = n1, number2 = n2
    print(add_result)

main()