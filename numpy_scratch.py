import numpy as np

data = np.linspace(1, 50, 11)
print(data)

result = np.all(data > 10)
print(result)
result = np.any(data > 10)
print(result)

result = np.all((data > 10) & (data < 100))  # NumPy verknüpft logische Ausdrücke mit & (UND-Verknüpfung) bzw. dem | (ODER), ~ Negation
print(result)
