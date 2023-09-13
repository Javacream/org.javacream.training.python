import numpy as np

data = np.linspace(1, 50, 11)

result = np.where((data < 30) & (data > 10))
print(result)

print(data[result])
