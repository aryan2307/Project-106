import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv(r"C:/Users/Admin/Downloads/Project 106/Data.csv")
fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
fig.show()
x = df["Coffee in ml"]
y = df["sleep in hours"]
corr = np.corrcoef(x,y)
print(corr)