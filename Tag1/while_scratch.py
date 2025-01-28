# Endlosschleife
#while True:
#    print('Hugo')

start = 4
end = 9
index = start
# ausführliche Formulieren
condition = index < end
while condition:
    print(index)
    index = index + 1
    condition = index < end
# gebräuchliche, kompakte Form
index = start
while index < end:
    print(index)
    index = index + 1
