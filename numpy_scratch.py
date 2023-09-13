import numpy as np

data = np.arange(0,10).reshape(2,5)

# Selection

selection = np.where(data < 5)

selection = data[0]

selection = data[:, 1]



