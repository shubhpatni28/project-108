import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("data.csv")

rate = df["Avg_Rating"].tolist()

fig = ff.create_distplot([rate],["Samsung"])
fig.show()