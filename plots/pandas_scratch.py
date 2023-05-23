import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv('./diamonds.csv')
#print(dataFrame.info())

#print(dataFrame[dataFrame['carat'] < 0.25])
#dataFrame.hist(column="carat", color="red", bins=20, range=(0, 4))
#dataFrame.boxplot(column="carat", by="clarity")
#dataFrame["carat"].plot(kind="density")
dataFrame.plot(kind="scatter", x="carat", y="price")
plt.savefig('scratch.png')

