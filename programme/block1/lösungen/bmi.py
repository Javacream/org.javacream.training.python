height = input("Bitte Körpergröße in Meter eingeben, z.B. 1.83: ")
height = float(height)

weight = float(input("Bitte Körpergewicht in Kilogramm eingeben, z.B. 74.88: "))

bmi = weight/(height*height)

print(f'Der Body Mass Index einer Person mit dem Körpergewicht {weight} und der Körpergröße {height} ist {bmi}')
