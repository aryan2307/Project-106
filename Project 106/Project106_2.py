import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv(r"C:/Users/Admin/Downloads/Project 106/Data2.csv")
fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
fig.show()
x = df["Marks In Percentage"]
y = df["Days Present"]
corr = np.corrcoef(x,y)
print(corr)