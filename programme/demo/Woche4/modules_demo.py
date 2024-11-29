import math # math ist eine Referenz auf das im Heap angelegte Modul

def perimeter(radius: float):
    result = 2 * radius * math.pi
    return result

def main():
    print(perimeter(2.2))


main()