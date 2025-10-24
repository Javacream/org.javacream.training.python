try:
    n = input ("Bitte Endzahl angeben:")
    n = int(n)
    numbers = dict()
    for i in range (1, n+1):
        numbers[i] = i**2
    print(numbers)    
except:
    print("Fehleingabe, n muss eine Zahl sein!")