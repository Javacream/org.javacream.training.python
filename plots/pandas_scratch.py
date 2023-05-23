import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv('./diamonds.csv')
#print(dataFrame.info())
dataFrame.hist(column="carat")

plt.savefig('scratch.png')
plt.savefig('scratch.pdf')

