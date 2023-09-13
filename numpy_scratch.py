import numpy as np

data1 = np.linspace(1, 50, 12).reshape(2,6)
data2 = np.linspace(42, 64, 12).reshape(2,6)
data3 = np.array([5])
data4 = 9
# Was ist das Ergebnis einer Addition dieser beiden Arrays?

# print(data1 + data2) # Elementweises +, -, *, /, funktioniert, weil beide Arrays die gleiche Form = shape haben
#print(data1 + data3)
print(data1 + data4)