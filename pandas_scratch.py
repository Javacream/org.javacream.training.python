import pandas as pd

series1 = pd.Series([1,2,3,4])
series2 = pd.Series([99, 11, 22, 7])

data_frame = pd.DataFrame([series1, series2])
data_frame.columns = ["A", "B", "C", "D"]
print (data_frame)