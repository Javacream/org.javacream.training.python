import pandas as pd

simple_series = pd.Series([1,2,3,4])
# simple_series = pd.Series(list('Hugo'))

# print(simple_series)

simple_series = pd.Series({'81371': 'München', '08122': 'Irgendwo'})
# print(simple_series)

simple_series.size
simple_series.shape
#print(simple_series.values)
print(simple_series.index)
