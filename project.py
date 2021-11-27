import pandas as pd 
import plotly.figure_factory as ff 

df = pd.read_csv("data2.csv")

#print(df)

rating_list = df["Avg Rating"].tolist()

graph = ff.create_distplot([rating_list],["rating distribution"],show_hist=False)
graph.show()