# Dieses Programm berechnet den Body Mass Index einer Person mit Gewicht 74.9 und Größe 183cm

name = input('Bitte Name eingeben: ')
weight = input('Bitte Körpergewicht eingeben: ')
height = input('Bitte Körpergröße angeben: ')

weight = float(weight)
height = int(height)

bmi = weight/(height*height)*100*100

# print("Die Person namens " + name + " hat einen BMI von " + bmi)
# print("Die Person namens " + name + " hat einen BMI von " + str(bmi))
print(f"Die Person namens {name} hat einen BMI von {bmi}")