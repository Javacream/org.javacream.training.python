number1 = 20
number2 = 22
result = number1 + number2
print(result) # 42: Das ist eine Lieblingszahl von EntwicklerInnen, Stichwprt Douglas Adams, Deep Thougth, Answer to all

result = 2*21
print(result)
print(84/2)

result = "Hello " + "World!"
print(result)

#result = "Hello " + number1# error, mischen von Typen ist nicht zulässig
result = 2*10+22 # Punkt vor Strich-Regel
print(result)

result = 2*(10 + 11)#Klammerung 
print(result)

print(1 + 1/3) # ergebnis ist eine Kommazahl

print((1 + 1/3)*3)


#result = 2*(3-5/2)+47 - 3/2 + 7*5 # syntaktisch OK, aber unwartbarer Code

# Kryptisch
z1 = 12
z2 = .19
z3 = z1*(1+z2)

# selbstdokumentierender Code
netto = 12
mehrwertSteuerInProzent = .19
aufschlag = 1 + mehrwertSteuerInProzent
brutto = netto * aufschlag
print(brutto)


